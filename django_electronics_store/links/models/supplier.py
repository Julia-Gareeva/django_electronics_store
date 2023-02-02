from django.db import models


class Supplier(models.Model):
    """Описание модели поставщики."""
    class Meta:
        verbose_name = "Поставщик"
        verbose_name_plural = "Поставщики"

    class NameSupplier(models.IntegerChoices):
        factory = 1, "Завод"
        distributor = 2, "Дистрибьютор"
        dealership = 3, "Дилерский центр"
        retailchain = 4, "Крупная розничная сеть"
        individualentrepreneur = 5, "Индивидуальный предприниматель"

    name = models.PositiveSmallIntegerField(verbose_name="Название поставщика", max_length=33,
                                            choices=NameSupplier.choices, default=NameSupplier.factory)
    is_deleted = models.BooleanField(verbose_name="Удален", default=False)
