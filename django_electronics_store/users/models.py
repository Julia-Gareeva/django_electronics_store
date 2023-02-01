from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ADMIN = "admin"
    MEMBER = "member"
    MODERATOR = "moderator"
    STAFF = "staff"
    ROLES = [
        (ADMIN, "администратор"),
        (MEMBER, "пользователь"),
        (MODERATOR, "модератор"),
        (STAFF, "персонал")
    ]
    MALE = "Male"
    FEMALE = "Female"
    SEX = [(MALE, "Мужской"), (FEMALE, "Женский")]

    first_name = models.CharField(verbose_name="Имя", max_length=100, null=True)
    last_name = models.CharField(verbose_name="Фамилия", max_length=150, null=True)
    username = models.CharField(verbose_name="Никнейм", max_length=55, unique=True)
    password = models.CharField(verbose_name="Пароль", max_length=90)
    role = models.CharField(verbose_name="Роль пользователя", max_length=10, choices=ROLES, default="member")
    age = models.SmallIntegerField(verbose_name="Возраст", max_length=3)
    sex = models.CharField(verbose_name="Пол человека", max_length=10, choices=SEX, default=FEMALE)
    email = models.EmailField(verbose_name="Электронная почта", max_length=55)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["username"]

    def __str__(self):
        return self.username
