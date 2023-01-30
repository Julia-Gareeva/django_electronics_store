from django.db import models

from django_electronics_store.links.models import Factories, Distributors, Dealerships, RetailChains, \
    IndividualEntrepreneurs


class Supplier(models.Model):
    """Описание модели поставщики."""
    class Meta:
        verbose_name = "Поставщик"
        verbose_name_plural = "Поставщики"

    id_supplier = models.ManyToManyField(Factories.Meta.verbose_name, Distributors.Meta.verbose_name,
                                         Dealerships.Meta.verbose_name, RetailChains.Meta.verbose_name,
                                         IndividualEntrepreneurs.Meta.verbose_name, verbose_name="ID поставщика")
    name = models.ManyToManyField(Factories.name, Distributors.name, Dealerships.name,
                                  RetailChains.name, IndividualEntrepreneurs.name,
                                  verbose_name="Название поставщика")
