from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView

from rest_framework import permissions, filters
from rest_framework.pagination import LimitOffsetPagination

from django_electronics_store.links.models import Factories
from django_electronics_store.links.permissions import FactoriesPermissions
from django_electronics_store.links.serializers import FactoriesCreateSerializer, FactoriesSerializer


# 4. Используя DRF, создать набор представлений:
#     4.1 Информацию обо всех объектах сети;
#     4.2 Информацию об объектах определённой страны (фильтр по названию);
#     4.3 Статистику об объектах, задолженность которых превышает среднюю задолженность всех объектов;
#     4.4 Все объекты сети, где можно встретить определённый продукт (фильтр по id продукта);
#     4.5 Возможность создания и удаления объекта сети и продукта;
#     4.6 Возможность обновления данных объекта сети и продукта (запретить обновление через API поля «Задолженность перед поставщиком»);


class FactoriesCreateView(CreateAPIView):
    model = Factories
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FactoriesCreateSerializer


class FactoriesListView(ListAPIView):
    model = Factories
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FactoriesSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    ordering_fields = ["name"]
    ordering = ["name"]
    search_fields = ["name", "contacts.address", "products.id"]

    def get_queryset(self):
        return Factories.objects.filter(
            participants__user=self.request.user, is_deleted=False
        )


class FactoriesView(RetrieveUpdateDestroyAPIView):
    model = Factories
    serializer_class = FactoriesSerializer
    permission_classes = [permissions.IsAuthenticated, FactoriesPermissions]

    def get_queryset(self):
        return Factories.objects.filter(
            participants__user=self.request.user, is_deleted=False
        )

    def perform_destroy(self, instance: Factories):
        # ...
        pass
