from django.shortcuts import render
from knox.views import LoginView as KnoxLoginView
from rest_framework import permissions
from django.contrib.auth import login
from .serializers import AuthTokenSerializer
# Create your views here.


class LoginView(KnoxLoginView):
    # serializer_class = LoginSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']  # type:ignore

        login(request, user)

        return super(LoginView, self).post(request, format=None)
