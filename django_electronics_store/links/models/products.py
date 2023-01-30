from django.db import models


class Products(models.Model):
    """Описание модели продукты."""
    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    name = models.CharField(verbose_name="Название", max_length=200)
    model = models.TextField(verbose_name="Модель", max_length=80)
    date_release_to_market = models.DateTimeField(verbose_name="Дата выхода продукта на рынок",
                                                  auto_now_add=True, input_formats=['%m/%d/%y %H:%M'])

    def __str__(self):
        return self.name
