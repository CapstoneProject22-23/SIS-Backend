from django.contrib import admin
from .models import Student, Teacher
from django import forms


class TeacherAdminForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = "__all__"
        widgets = {
            "user": forms.HiddenInput,  # Hide the user field in the admin form
        }

    def clean(self):
        cleaned_data = super().clean()
        cleaned_user = cleaned_data.get("user")

        if cleaned_user is None:
            # If the user field is not set, clear the error
            self._errors.pop("user", None)

        return cleaned_data

    def delete_model(self, request, obj):
        # Delete the associated user object when deleting the teacher
        obj.user.delete()
        obj.delete()


class TeacherAdmin(admin.ModelAdmin):
    form = TeacherAdminForm


class StudentAdminForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        widgets = {
            "user": forms.HiddenInput,  # Hide the user field in the admin form
        }

    def clean(self):
        cleaned_data = super().clean()
        cleaned_user = cleaned_data.get("user")

        if cleaned_user is None:
            # If the user field is not set, clear the error
            self._errors.pop("user", None)

        return cleaned_data


class StudentAdmin(admin.ModelAdmin):
    form = StudentAdminForm


# Register your models here.
admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)
