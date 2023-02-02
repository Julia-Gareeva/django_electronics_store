from django.db import models

from links.models.address import Address


class Contacts(models.Model):
    """Описание модели контакты."""
    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"

    email = models.EmailField(verbose_name="Электронная почта", max_length=45)
    address = models.ForeignKey(Address, verbose_name="Адрес", on_delete=models.CASCADE)

    def __str__(self):
        return self.email
