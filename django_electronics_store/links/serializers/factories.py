from rest_framework import serializers
from django.db import transaction

from django_electronics_store.links.models import Factories
from django_electronics_store.links.models.participant import FactoriesParticipant
from django_electronics_store.users.models import User


class FactoriesDetailSerializer(serializers.Serializer):
    """Сериализация одного объекта сети 'Завод'."""
    factories = FactoriesParticipant.factories.name
    # factories = FactoriesParticipant.VerboseName.choices

    class Meta:
        model = Factories
        fields = "__all__"
        read_only_fields = ("id", "name", "contacts", "products", "staff", "supplier", "arrears", "date")


class FactoriesListSerializer(serializers.ModelSerializer):
    """Сериализация списка объекта сети 'Завод'."""
    factories = FactoriesParticipant.factories.name
    # factories = FactoriesParticipant.VerboseName.choices

    class Meta:
        model = Factories
        fields = "__all__"
        read_only_fields = ("id", "name", "contacts", "products", "staff", "supplier", "arrears", "date")


class FactoriesCreateSerializer(serializers.ModelSerializer):
    """Сериализация создания объекта сети."""

    class Meta:
        model = Factories
        fields = "__all__"
        read_only_fields = ("id", "name", "contacts", "date")

    def create(self, validated_data):
        user = validated_data.pop("user")
        factories = Factories.objects.create(**validated_data)
        FactoriesParticipant.objects.create(
            user=user, factories=FactoriesParticipant.VerboseName.factories, role=FactoriesParticipant.Role.admin
        )
        return factories


class FactoriesParticipantSerializer(serializers.Serializer):
    """Сериализация модели 'участники'."""
    role = serializers.ChoiceField(
        required=True, choices=FactoriesParticipant.Role
    )
    user = serializers.SlugRelatedField(
        slug_field="username", queryset=User.objects.all()
    )

    class Meta:
        model = FactoriesParticipant
        fields = "__all__"
        read_only_fields = ("id", "factories", "role")


class FactoriesUpdateSerializer(serializers.ModelSerializer):
    """Сериализация обновления объекта 'завод'."""
    participants = FactoriesParticipantSerializer(many=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Factories
        fields = "__all__"
        read_only_fields = ("id", "name", "contacts", "products", "staff", "supplier", "arrears", "date")

    def update(self, instance, validated_data):
        admin = validated_data.pop("user")

        with transaction.atomic():
            # измените участников, если пройдено
            if validated_data.get("participants"):
                new_participants = validated_data.pop("participants")
                new_by_id = {part["user"].id: part for part in new_participants}
                old_participants = instance.participants.exclude(user=admin)

                for old_participant in old_participants:
                    if old_participant.user_id not in new_by_id:
                        old_participant.delete()
                    else:
                        if (old_participant.role
                                != new_by_id[old_participant.user_id]["role"]):
                            old_participant.role = new_by_id[old_participant.user_id]["role"]
                            old_participant.save()
                        new_by_id.pop(old_participant.user_id)

                for new_part in new_by_id.values():
                    FactoriesParticipant.objects.create(
                        board=instance, user=new_part["user"], role=new_part["role"]
                    )

            if validated_data.get('title'):
                instance.title = validated_data["title"]
            instance.save()
        return instance
