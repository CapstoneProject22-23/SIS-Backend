from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone


class CustomDateField(models.DateField):
    pass


class CustomUserManager(BaseUserManager):
    def create_user(self, enrollment_number, password=None, **extra_fields):
        if not enrollment_number:
            raise ValueError('The Enrollment Number must be provided')
        if len(str(enrollment_number)) != 10:
            raise ValueError('Enrollment number must be of 10 digits')

        user = self.model(enrollment_number=enrollment_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    enrollment_number = models.IntegerField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateField(default=timezone.localdate)
    date_of_birth = models.DateField(
        null=True, blank=True, default=timezone.localdate)

    USERNAME_FIELD = 'enrollment_number'

    objects = CustomUserManager()

    def __str__(self):
        return str(self.enrollment_number)
