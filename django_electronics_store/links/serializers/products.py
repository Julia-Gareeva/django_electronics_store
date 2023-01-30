from rest_framework import serializers

from django_electronics_store.links.models.products import Products


class ProductsSerializer(serializers.ModelSerializer):
    """Сериализация модели "продукты"."""
    class Meta:
        model = Products
        fields = "__all__"
        read_only_fields = ("id", "name", "model", "date_release_to_market")


class ProductsCreateSerializer(serializers.ModelSerializer):
    """Сериализация создания модели "продукты"."""
    class Meta:
        model = Products
        fields = "__all__"
        read_only_fields = ("id", "name", "model", "date_release_to_market")


class ProductsDeleteSerializer(serializers.ModelSerializer):
    """Сериализация удаления модели "продукты"."""
    class Meta:
        model = Products
        fields = "__all__"
        read_only_fields = ("id", "name", "model", "date_release_to_market")
