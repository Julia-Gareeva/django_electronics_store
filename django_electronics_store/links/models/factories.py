from django.db import models

from links.models.contacts import Contacts
from links.models.products import Products
from links.models.supplier import Supplier


class Factories(models.Model):
    """Описание модели заводы."""
    class Meta:
        verbose_name = "Завод"
        verbose_name_plural = "Заводы"

    name = models.CharField(verbose_name="Название", max_length=150)
    contacts = models.ManyToManyField(Contacts, verbose_name="Контакты")
    products = models.ManyToManyField(Products, verbose_name="Продукты")
    staff = models.TextField(verbose_name="Сотрудники")
    supplier = models.ManyToManyField(Supplier, verbose_name="Поставщик")
    arrears = models.FloatField(verbose_name="Задолженность перед поставщиком")
    date = models.DateTimeField(verbose_name="Время создания", auto_now_add=True) # input_formats=['%m/%d/%y %H:%M']

    def __str__(self):
        return self.name


class Distributors(Factories):
    """Описание модели дистрибьютор."""
    class Meta:
        verbose_name = "Дистрибьютор"
        verbose_name_plural = "Дистрибьюторы"


class Dealerships(Factories):
    """Описание модели дилерский центр."""
    class Meta:
        verbose_name = "Дилерский центр"
        verbose_name_plural = "Дилерские центры"


class RetailChains(Factories):
    """Описание модели крупная розничная сеть."""
    class Meta:
        verbose_name = "Крупная розничная сеть"
        verbose_name_plural = "Крупные розничные сети"


class IndividualEntrepreneurs(Factories):
    """Описание модели индивидуальный предприниматель."""
    class Meta:
        verbose_name = "Индивидуальный предприниматель"
        verbose_name_plural = "Индивидуальные предприниматели"
