# Generated by Django 4.1.7 on 2023-05-10 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_alter_student_contact_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='semester',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
