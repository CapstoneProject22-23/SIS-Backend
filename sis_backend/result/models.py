from django.db import models
from users.models import Student
import os
from django.utils.text import get_valid_filename


def result_file_upload_to(instance, filename):
    # Generate a new file name using the student's enrollment number
    enrollment_number = instance.student.enrollment_number
    new_filename = f"RESULT_{instance.exam}_{instance.year}.pdf"

    # Return the updated file path
    return f"students/{enrollment_number}/results/{new_filename}"


# Create your models here.
class Result(models.Model):
    EXAM_CHOICES = [
        ("summer", "SUMMER"),
        ("winter", "WINTER"),
    ]

    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="results"
    )
    result_file = models.FileField(upload_to=result_file_upload_to)
    exam = models.CharField(max_length=20, choices=EXAM_CHOICES)
    year = models.PositiveIntegerField()

    def __str__(self):
        return f"Result_{self.student.enrollment_number}_{self.exam}_{self.year}"
