from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from django_electronics_store.users.models import User


class UserSerializer(serializers.ModelSerializer):
    """Сериализация модели 'пользователь'."""
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "username", "email", "password"]

    def is_valid(self, raise_exception=False):
        """Получить пароль, повторить и удалить из исходных данных."""
        self._password_repeat = self.initial_data.pop('password_repeat')
        return super().is_valid(raise_exception=raise_exception)

    def validate_username(self, value):
        """Убедитесь, что имя пользователя не существует."""
        if self.Meta.model.objects.filter(username=value).exists():
            raise serializers.ValidationError(['Пользователь с таким именем пользователя уже существует.'])
        return value

    def validate_password(self, value):
        """Убедитесь, что пароль действителен."""
        validate_password(value)
        return value

    def validate(self, data):
        """Убедитесь, что пароли совпадают."""
        print(data.get('password'))
        print(self._password_repeat)
        if data.get('password') != self._password_repeat:
            raise serializers.ValidationError({'password_repeat': ['Пароли должны совпадать.']})
        return data

    def create(self, validated_data):
        """Создать пользователя."""
        user = User.objects.create(**validated_data)
        user.set_password(user.password)
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    """Сериализатор входа в систему."""
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    def validate_username(self, value):
        """Убедитесь, что имя пользователя существует."""
        if not User.objects.filter(username=value).exists():
            raise serializers.ValidationError(["Пользователь с таким именем пользователя не существует."])
        return value


class RetrieveUpdateSerializer(serializers.ModelSerializer):
    """Сериализатор для того, чтобы извлекать обновление."""
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(required=False, max_length=55)
    first_name = serializers.CharField(required=False, allow_blank=True, max_length=100)
    last_name = serializers.CharField(required=False, allow_blank=True, max_length=150)
    email = serializers.EmailField(required=False, allow_blank=True)

    def validate_username(self, value):
        """Убедитесь, что имя пользователя не существует."""
        # получить текущего пользователя
        current_user = self.context['request'].user

        # проверьте, что имя пользователя не существует, если это не текущий пользователь
        if self.Meta.model.objects.filter(username=value).exists() and current_user.username != value:
            raise serializers.ValidationError(['Пользователь с таким именем пользователя уже существует.'])
        return value

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']


class PasswordUpdateSerializer(serializers.Serializer):
    """Сериализатор обновления пароля."""
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_new_password(self, value):
        validate_password(value)
        return value
