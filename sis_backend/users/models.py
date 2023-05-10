from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_delete
from django.dispatch import receiver

# Create your models here.


class Branches(models.TextChoices):
    CO = "CO", "Computer Engineering"
    EE = "EE", "Electrical Engineering"
    ET = "ET", "Electronics and Telecommunication Engineering"
    CE = "CE", "Civil Engineering"
    ME = "ME", "Mechanical Engineering"


class Student(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="student", null=True, blank=True
    )
    enrollment_number = models.IntegerField(primary_key=True, max_length=12)
    roll_no = models.IntegerField(null=True)
    first_name = models.CharField(max_length=50, null=False)
    fathers_name = models.CharField(max_length=50, blank=True)
    mothers_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=50, null=False)
    dob = models.DateField(null=True)
    birth_place = models.CharField(max_length=100, null=True, blank=True)
    admission_date = models.DateField(null=True)
    year = models.IntegerField(default=1)
    branch = models.CharField(max_length=2, choices=Branches.choices)
    semester = models.IntegerField(null=True, blank=True)
    scheme = models.CharField(max_length=1, default="I")
    contact_no = models.BigIntegerField(blank=True, null=True)
    address = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=50, null=True, blank=True)
    sub_category = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return str(self.enrollment_number)

    def save(self, *args, **kwargs):
        if self.pk is not None and self.user_id is None:
            # Retrieve the associated User object
            user = User.objects.filter(username=self.enrollment_number).first()
            if user is not None:
                # Delete the associated User object
                user.delete()
        # Check if the student is being created for the first time
        if not self.user:
            # Create a corresponding User object for the student
            user = User.objects.create_user(username=self.enrollment_number)
            user.set_unusable_password()
            user.save()
            self.user = user

        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.user:
            self.user.delete()
        return super().delete(*args, **kwargs)


class Teacher(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="teachers", null=True, blank=True
    )
    faculty_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    contact_no = models.BigIntegerField(blank=True)
    dob = models.DateField(null=True)
    doj = models.DateField(null=True)
    branch = models.CharField(max_length=2, choices=Branches.choices)
    faculty_type = models.CharField(max_length=20)
    post = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

    def save(self, *args, **kwargs):
        if self.pk is not None and self.user_id is None:
            # Retrieve the associated User object
            user = User.objects.filter(username=self.faculty_id).first()
            if user is not None:
                # Delete the associated User object
                user.delete()

        # Check if the student is being created for the first time
        if not self.user:
            # Create a corresponding User object for the student
            user = User.objects.create_user(username=self.faculty_id, is_staff=True)
            user.set_unusable_password()
            user.save()
            self.user = user

        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.user:
            self.user.delete()
        return super().delete(*args, **kwargs)
