from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import serializers, viewsets
from .models import Result
from users.models import Student
from .serializers import ResultSerializer
import os
from rest_framework.views import Response
from rest_framework import status
from rest_framework import permissions
from django.conf import settings


# Create your views here.
class ResultViewSet(viewsets.ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        # Get the student based on the logged-in user or any other identifier
        student = request.user.student
        # Create the result object
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        result = serializer.save(student=student)

        # Rename and store the file
        exam = serializer.validated_data.get("exam")
        year = serializer.validated_data.get("year")
        file_name = f"RESULT_{exam}_{year}.pdf"

        # Create the student's result directory if it doesn't exist
        # student_directory = f"media/students/{student.enrollment_number}/results"
        # os.makedirs(student_directory, exist_ok=True)

        # Save the uploaded file to the student's result directory
        # file_path = os.path.join(student_directory, file_name)
        # with open(file_path, "wb") as file:
        #     file.write(request.data["result_file"].read())

        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )


class RetrieveResultsView(APIView):
    # permission_classes = (permissions.IsAuthenticated,)
    def get(self, request):
        student = request.user.student

        results = student.results.all()

        response = dict()

        for result in results:
            download_url = os.path.join(
                settings.MEDIA_ROOT,
                "students",
                f"{student.enrollment_number}",
                "results",
                f"RESULT_{result.exam}_{result.year}.pdf",
            )
            download_link = (
                "http://localhost:8000/"
                + settings.MEDIA_URL
                + "students/"
                + f"{student.enrollment_number}/"
                + "results/"
                + f"RESULT_{result.exam}_{result.year}.pdf"
            )
            response[f"{result.exam} {result.year}"] = download_link
            print(result.year)

        return Response(response)
