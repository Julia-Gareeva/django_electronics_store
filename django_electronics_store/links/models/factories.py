from django.db import models

from links.models.contacts import Contacts
from links.models.products import Products
from links.models.supplier import Supplier

from users.models import User


class Factories(models.Model):
    """Описание модели заводы."""
    class Meta:
        verbose_name = "Завод"
        verbose_name_plural = "Заводы"

    name = models.CharField(verbose_name="Название", max_length=150)
    contacts = models.ForeignKey(Contacts, verbose_name="Контакты", on_delete=models.CASCADE)
    products = models.ManyToManyField(Products, verbose_name="Продукты", on_delete=models.CASCADE)
    staff = models.ForeignKey(User, verbose_name="Сотрудники", on_delete=models.PROTECT)
    supplier = models.ForeignKey(Supplier, verbose_name="Поставщик", on_delete=models.PROTECT)
    arrears = models.FloatField(verbose_name="Задолженность перед поставщиком")
    date = models.DateTimeField(verbose_name="Время создания", auto_now_add=True)

    def __str__(self):
        return self.name


class Distributors(models.Model):
    """Описание модели дистрибьютор."""
    class Meta:
        verbose_name = "Дистрибьютор"
        verbose_name_plural = "Дистрибьюторы"

    name = models.CharField(verbose_name="Название", max_length=150)
    contacts = models.ForeignKey(Contacts, verbose_name="Контакты", on_delete=models.CASCADE)
    products = models.ManyToManyField(Products, verbose_name="Продукты", on_delete=models.CASCADE)
    staff = models.ForeignKey(User, verbose_name="Сотрудники", on_delete=models.PROTECT)
    supplier = models.ForeignKey(Supplier, verbose_name="Поставщик", on_delete=models.PROTECT)
    arrears = models.FloatField(verbose_name="Задолженность перед поставщиком")
    date = models.DateTimeField(verbose_name="Время создания", auto_now_add=True)

    def __str__(self):
        return self.name


class Dealerships(models.Model):
    """Описание модели дилерский центр."""
    class Meta:
        verbose_name = "Дилерский центр"
        verbose_name_plural = "Дилерские центры"

    name = models.CharField(verbose_name="Название", max_length=150)
    contacts = models.ForeignKey(Contacts, verbose_name="Контакты", on_delete=models.CASCADE)
    products = models.ManyToManyField(Products, verbose_name="Продукты", on_delete=models.CASCADE)
    staff = models.ForeignKey(User, verbose_name="Сотрудники", on_delete=models.PROTECT)
    supplier = models.ForeignKey(Supplier, verbose_name="Поставщик", on_delete=models.PROTECT)
    arrears = models.FloatField(verbose_name="Задолженность перед поставщиком")
    date = models.DateTimeField(verbose_name="Время создания", auto_now_add=True)

    def __str__(self):
        return self.name


class RetailChains(models.Model):
    """Описание модели крупная розничная сеть."""
    class Meta:
        verbose_name = "Крупная розничная сеть"
        verbose_name_plural = "Крупные розничные сети"

    name = models.CharField(verbose_name="Название", max_length=150)
    contacts = models.ForeignKey(Contacts, verbose_name="Контакты", on_delete=models.CASCADE)
    products = models.ManyToManyField(Products, verbose_name="Продукты", on_delete=models.CASCADE)
    staff = models.ForeignKey(User, verbose_name="Сотрудники", on_delete=models.PROTECT)
    supplier = models.ForeignKey(Supplier, verbose_name="Поставщик", on_delete=models.PROTECT)
    arrears = models.FloatField(verbose_name="Задолженность перед поставщиком")
    date = models.DateTimeField(verbose_name="Время создания", auto_now_add=True)

    def __str__(self):
        return self.name


class IndividualEntrepreneurs(models.Model):
    """Описание модели индивидуальный предприниматель."""
    class Meta:
        verbose_name = "Индивидуальный предприниматель"
        verbose_name_plural = "Индивидуальные предприниматели"

    name = models.CharField(verbose_name="Название", max_length=150)
    contacts = models.ForeignKey(Contacts, verbose_name="Контакты", on_delete=models.CASCADE)
    products = models.ManyToManyField(Products, verbose_name="Продукты", on_delete=models.CASCADE)
    staff = models.ForeignKey(User, verbose_name="Сотрудники", on_delete=models.PROTECT)
    supplier = models.ForeignKey(Supplier, verbose_name="Поставщик", on_delete=models.PROTECT)
    arrears = models.FloatField(verbose_name="Задолженность перед поставщиком")
    date = models.DateTimeField(verbose_name="Время создания", auto_now_add=True)

    def __str__(self):
        return self.name
