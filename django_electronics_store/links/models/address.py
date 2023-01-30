from django.db import models


class Address(models.Model):
    """Описание модели адрес."""
    class Meta:
        verbose_name = "Адрес"
        verbose_name_plural = "Адреса"

    country = models.TextField(verbose_name="Страна", max_length=55)
    city = models.TextField(verbose_name="Город", max_length=55)
    street = models.TextField(verbose_name="Улица", max_length=55)
    house_number = models.IntegerField(verbose_name="Номер дома")

    def __str__(self):
        return self.country
