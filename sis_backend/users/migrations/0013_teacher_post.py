# Generated by Django 4.1.7 on 2023-05-10 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_student_semester'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='post',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
