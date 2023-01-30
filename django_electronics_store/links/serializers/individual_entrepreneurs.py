from django_electronics_store.links.models import IndividualEntrepreneurs
from django_electronics_store.links.serializers.factories import FactoriesDetailSerializer, FactoriesListSerializer, \
    FactoriesCreateSerializer, FactoriesUpdateSerializer


class IndividualEntrepreneursDetailSerializer(FactoriesDetailSerializer):
    """Сериализация одного объекта сети 'Индивидуальный предприниматель'."""
    class Meta:
        model = IndividualEntrepreneurs
        fields = "__all__"


class IndividualEntrepreneursListSerializer(FactoriesListSerializer):
    """Сериализация списка объекта сети 'Индивидуальный предприниматель'."""
    class Meta:
        model = IndividualEntrepreneurs
        fields = "__all__"


class IndividualEntrepreneursCreateSerializer(FactoriesCreateSerializer):
    """Сериализация создания объекта сети."""
    class Meta:
        model = IndividualEntrepreneurs
        fields = "__all__"


class IndividualEntrepreneursUpdateSerializer(FactoriesUpdateSerializer):
    """Сериализация обновления объекта сети."""
    class Meta:
        model = IndividualEntrepreneurs
        fields = "__all__"
