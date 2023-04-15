from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser
import datetime
from django.utils import timezone
# Register your models here.


class CustomUserDateOfBirth(admin.ModelAdmin):
    def date_of_birth(self, obj):
        return obj.date_of_birth.astimezone(timezone.get_default_timezone())

    date_of_birth.short_description = 'Date of birth'


class UserAdmin(BaseUserAdmin, CustomUserDateOfBirth):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name',
         'last_name', 'enrollment_number', 'date_of_birth')}),
        ('Permissions', {'fields': ('is_staff',
         'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )

    list_display = ('enrollment_number', 'email', 'first_name', 'last_name',
                    'date_of_birth')

    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)

    list_filter = ('is_staff', 'is_superuser', 'groups')


admin.site.register(CustomUser, UserAdmin)
