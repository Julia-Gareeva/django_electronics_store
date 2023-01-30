from django_electronics_store.links.models import RetailChains
from django_electronics_store.links.serializers.factories import FactoriesDetailSerializer, FactoriesListSerializer, \
    FactoriesCreateSerializer, FactoriesUpdateSerializer


class RetailChainsDetailSerializer(FactoriesDetailSerializer):
    """Сериализация одного объекта сети 'Крупная розничная сеть'."""
    class Meta:
        model = RetailChains
        fields = "__all__"


class RetailChainsListSerializer(FactoriesListSerializer):
    """Сериализация списка объекта сети 'Крупная розничная сеть'."""
    class Meta:
        model = RetailChains
        fields = "__all__"


class RetailChainsCreateSerializer(FactoriesCreateSerializer):
    """Сериализация создания объекта сети."""
    class Meta:
        model = RetailChains
        fields = "__all__"


class RetailChainsUpdateSerializer(FactoriesUpdateSerializer):
    """Сериализация обновления объекта сети."""
    class Meta:
        model = RetailChains
        fields = "__all__"
