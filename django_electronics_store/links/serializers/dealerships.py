from django_electronics_store.links.models import Dealerships
from django_electronics_store.links.serializers.factories import FactoriesDetailSerializer, FactoriesListSerializer, \
    FactoriesCreateSerializer, FactoriesUpdateSerializer


class DealershipsDetailSerializer(FactoriesDetailSerializer):
    """Сериализация одного объекта сети 'Дилерский центр'."""
    class Meta:
        model = Dealerships
        fields = "__all__"


class DealershipsListSerializer(FactoriesListSerializer):
    """Сериализация списка объекта сети 'Дилерский центр'."""
    class Meta:
        model = Dealerships
        fields = "__all__"


class DealershipsCreateSerializer(FactoriesCreateSerializer):
    """Сериализация создания объекта сети."""
    class Meta:
        model = Dealerships
        fields = "__all__"


class DealershipsUpdateSerializer(FactoriesUpdateSerializer):
    """Сериализация обновления объекта сети."""
    class Meta:
        model = Dealerships
        fields = "__all__"
