from django.db import models

from django_electronics_store.users.models import User
from django_electronics_store.links.models import Factories


class FactoriesParticipant(models.Model):
    class Meta:
        unique_together = ("factories", "user")
        verbose_name = "Участник"
        verbose_name_plural = "Участники"

    class Role(models.IntegerChoices):
        admin = 1, "Админ"
        member = 2, "Пользователь"
        moderator = 3, "Модератор"
        staff = 4, "Персонал"

    class VerboseName(models.IntegerChoices):
        factories = 1, "Завод"
        distributors = 2, "Дистрибьютор"
        dealerships = 3, "Дилерский центр"
        retailchains = 4, "Крупная розничная сеть"
        individualentrepreneurs = 5, "Индивидуальный предприниматель"

    factories = models.ForeignKey(
        Factories,
        verbose_name="Название",
        choices=VerboseName.choices,
        default=VerboseName.factories,
        on_delete=models.PROTECT,
        related_name="participants",
    )
    user = models.ForeignKey(
        User,
        verbose_name="Пользователь",
        on_delete=models.PROTECT,
        related_name="participants",
    )
    role = models.PositiveSmallIntegerField(
        verbose_name="Роль", choices=Role.choices, default=Role.admin
    )
