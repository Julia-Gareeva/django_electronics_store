from django.db import models


class Supplier(models.Model):
    """Описание модели поставщики."""
    class Meta:
        verbose_name = "Поставщик"
        verbose_name_plural = "Поставщики"

    FACTORY = "Factory"
    DISTRIBUTOR = "Distributor"
    DEALERSHIP = "Dealership"
    RETAILCHAIN = "Retailchain"
    INDIVIDUALENTREPRENEUR = "Individualentrepreneur"

    SUPPLIER_NAME = [
        (FACTORY, "Завод"),
        (DISTRIBUTOR, "Дистрибьютор"),
        (DEALERSHIP, "Дилерский центр", ),
        (RETAILCHAIN, "Крупная розничная сеть"),
        (INDIVIDUALENTREPRENEUR, "Индивидуальный предприниматель")
    ]

    name = models.TextField(verbose_name="Название поставщика", max_length=33, choices=SUPPLIER_NAME, default=FACTORY)
