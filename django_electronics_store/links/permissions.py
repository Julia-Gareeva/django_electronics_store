from rest_framework import permissions

from links.models.participant import FactoriesParticipant


class BasePermissionMixin(permissions.IsAuthenticated):
    roles = [FactoriesParticipant.Role.admin, FactoriesParticipant.Role.member,
             FactoriesParticipant.Role.moderator, FactoriesParticipant.Role.staff]

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return FactoriesParticipant.objects.filter(
                user=request.user,
                factories=obj
            ).exists()

        return FactoriesParticipant.objects.filter(
            user=request.user,
            factories=obj,
            role__in=self.roles
        ).exists()


class FactoriesPermissions(BasePermissionMixin):
    """Разрешения для модели "Завод"."""
    roles = [FactoriesParticipant.Role.admin,
             FactoriesParticipant.Role.moderator]

    def has_object_permission(self, request, view, obj):
        return super().has_object_permission(request, view, obj=obj)


class DistributorsPermissions(BasePermissionMixin):
    """Разрешения для модели "Дистрибьютор"."""
    roles = [FactoriesParticipant.Role.admin,
             FactoriesParticipant.Role.moderator]

    def has_object_permission(self, request, view, obj):
        return super().has_object_permission(request, view, obj=obj)


class DealershipsPermissions(BasePermissionMixin):
    """Разрешения для модели "Дилерский центр"."""
    roles = [FactoriesParticipant.Role.admin,
             FactoriesParticipant.Role.moderator]

    def has_object_permission(self, request, view, obj):
        return super().has_object_permission(request, view, obj=obj)


class RetailChainsPermissions(BasePermissionMixin):
    """Разрешения для модели "Крупная розничная сеть"."""
    roles = [FactoriesParticipant.Role.admin,
             FactoriesParticipant.Role.moderator]

    def has_object_permission(self, request, view, obj):
        return super().has_object_permission(request, view, obj=obj)


class IndividualEntrepreneursPermissions(BasePermissionMixin):
    """Разрешения для модели "Индивидуальный предприниматель"."""
    roles = [FactoriesParticipant.Role.admin,
             FactoriesParticipant.Role.moderator]

    def has_object_permission(self, request, view, obj):
        return super().has_object_permission(request, view, obj=obj)
