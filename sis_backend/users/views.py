from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView
from .models import Student, Teacher
from rest_framework import permissions
from .serializers import StudentSerializer, TeacherSerializer
# Create your views here.


class StudentProfile(RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class TeacherProfile(RetrieveAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
