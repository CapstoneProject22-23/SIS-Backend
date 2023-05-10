from django.urls import path
from .views import StudentProfile, TeacherProfile
app_name = 'users'

urlpatterns = [
    path('student/<int:pk>',
         StudentProfile.as_view(), name='student-profile'),
    path('teacher/<int:pk>', TeacherProfile.as_view(), name='teacher-profile'),
]
