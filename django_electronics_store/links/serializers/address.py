from rest_framework import serializers

from django_electronics_store.links.models.address import Address


class AddressSerializer(serializers.ModelSerializer):
    """Сериализация модели "адреса"."""
    class Meta:
        model = Address
        fields = "__all__"
        read_only_field = ("id", "country", "city", "street", "house_number")
