from rest_framework import serializers

from django_electronics_store.links.models.supplier import Supplier


class SupplierSerializer(serializers.ModelSerializer):
    """Сериализация объекта "поставщики"."""
    class Meta:
        model = Supplier
        fields = "__all__"
        read_only_fields = ("id", "id_supplier", "name")
