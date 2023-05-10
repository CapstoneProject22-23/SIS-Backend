from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from .models import Student, Teacher
User = get_user_model()


class UserTypeAuthenticationBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        # Check if the user type is specified
        user_type = kwargs.get('user_type')

        if user_type == 'student':
            # Authenticate the student based on the enrollment number
            try:
                student = Student.objects.get(enrollment_number=username)
                user = student.user

                if user.check_password(password):
                    return user

            except Student.DoesNotExist:
                return None

        elif user_type == 'teacher':
            # Authenticate the teacher based on the username
            try:
                teacher = Teacher.objects.get(faculty_id=username)
                user = teacher.user

                if user.check_password(password):
                    return user

            except Teacher.DoesNotExist:
                return None

        return None
