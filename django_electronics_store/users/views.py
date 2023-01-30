from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer, RetrieveUpdateSerializer, PasswordUpdateSerializer, LoginSerializer


class SignUpView(CreateAPIView):
    """Создать нового пользователя."""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LoginView(CreateAPIView):
    """Вход в систему пользователя."""
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        # проверка запроса данных
        serializer = self.get_serializer(data=request.data)

        if not serializer.is_valid():
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # аутентификация
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)

        # авторизация
        if user:
            login(request, user)
            return Response(status=status.HTTP_200_OK)

        return Response(data={'password': ['Неверный пароль.']}, status=status.HTTP_400_BAD_REQUEST)


class UserRetrieveUpdateView(RetrieveUpdateDestroyAPIView):
    """Представление извлечения пользователя, обновление."""
    queryset = User.objects.all()
    serializer_class = RetrieveUpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

    def delete(self, request, *args, **kwargs):
        logout(request)
        return Response(status=status.HTTP_200_OK)


class PasswordUpdateView(UpdateAPIView):
    """Представление обновления пароля."""
    serializer_class = PasswordUpdateSerializer
    model = User
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get('old_password')):
                return Response({"old_password": ["Неверный пароль, пожалуйста, попробуйте еще раз."]},
                                status=status.HTTP_400_BAD_REQUEST)
            self.object.set_password(serializer.data.get('new_password'))
            self.object.save()
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
