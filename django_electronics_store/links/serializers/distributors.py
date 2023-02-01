from links.models import Distributors
from links.serializers.factories import FactoriesListSerializer, FactoriesDetailSerializer, \
    FactoriesCreateSerializer, FactoriesUpdateSerializer


class DistributorsDetailSerializer(FactoriesDetailSerializer):
    """Сериализация одного объекта сети 'Дистрибьютор'."""
    class Meta:
        model = Distributors
        fields = "__all__"


class DistributorsListSerializer(FactoriesListSerializer):
    """Сериализация списка объекта сети 'Дистрибьютор'."""
    class Meta:
        model = Distributors
        fields = "__all__"


class DistributorsCreateSerializer(FactoriesCreateSerializer):
    """Сериализация создания объекта сети."""
    class Meta:
        model = Distributors
        fields = "__all__"


class DistributorsUpdateSerializer(FactoriesUpdateSerializer):
    """Сериализация обновления объекта сети."""
    class Meta:
        model = Distributors
        fields = "__all__"
