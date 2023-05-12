from rest_framework import serializers, viewsets
from .models import Result
from users.models import Student
from rest_framework.views import Response
import os
from rest_framework import status


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = ["id", "student", "result_file", "exam", "year"]
        read_only_fields = ["id"]
