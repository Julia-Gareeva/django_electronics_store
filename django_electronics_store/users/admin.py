from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):

    # настройка отображения формы пользователя
    fieldsets = (
        (('General info'), {
            'fields': ('username', 'first_name', 'last_name', 'email')
        }),
        (('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser'),
        }),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    list_display = ('username', 'email', 'first_name', 'last_name')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    list_filter = ('is_staff', 'is_superuser', 'is_active')

    # установите для некоторых полей значение только для чтения при просмотре формы
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['last_login', 'date_joined']
        return self.readonly_fields
