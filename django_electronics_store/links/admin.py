from django.contrib import admin

from django_electronics_store.links.models import Factories, Distributors, Dealerships, \
    RetailChains, IndividualEntrepreneurs
from django_electronics_store.links.models.address import Address
from django_electronics_store.links.models.contacts import Contacts
from django_electronics_store.links.models.products import Products
from django_electronics_store.links.models.supplier import Supplier


class BaseAdmin(admin.ModelAdmin):
    """Базовая админ панель."""
    list_display = ("name", "contacts", "products", "staff", "supplier", "arrears", "date")
    search_fields = ("name", "products", "arrears", "date")
    readonly_fields = ("contacts", "staff", "supplier", "arrears")


class FactoriesAdmin(BaseAdmin):
    """Админ панель - Заводы."""
    pass


class DistributorsAdmin(BaseAdmin):
    """Админ панель - Дистрибьюторы."""
    pass


class DealershipsAdmin(BaseAdmin):
    """Админ панель - Дилерские центры."""
    pass


class RetailChainsAdmin(BaseAdmin):
    """Админ панель - Крупные розничные сети."""
    pass


class IndividualEntrepreneursAdmin(BaseAdmin):
    """Админ панель - Индивидуальные предприниматели."""
    pass


class SupplierAdmin(BaseAdmin):
    """Админ панель - Поставщики."""
    list_display = ("id_supplier", "name")
    search_fields = ("id_supplier", "name")
    readonly_fields = ("id_supplier", "name")


admin.site.register(Factories, FactoriesAdmin)
admin.site.register(Address, FactoriesAdmin)
admin.site.register(Contacts, FactoriesAdmin)
admin.site.register(Products, FactoriesAdmin)
admin.site.register(Distributors, DistributorsAdmin)
admin.site.register(Dealerships, DealershipsAdmin)
admin.site.register(RetailChains, RetailChainsAdmin)
admin.site.register(IndividualEntrepreneurs, IndividualEntrepreneursAdmin)
admin.site.register(Supplier, SupplierAdmin)
