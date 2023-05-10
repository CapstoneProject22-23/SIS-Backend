from django.urls import path
from .views import LoginView
from knox.views import LogoutView
app_name = 'auth_api'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login-user'),
    path('logout/', LogoutView.as_view(), name='logout-user')
]
