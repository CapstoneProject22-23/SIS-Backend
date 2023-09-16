from django.shortcuts import render
from rest_framework.views import APIView, Response
from django.http import FileResponse
from rest_framework import permissions
from PyPDF2 import PdfReader, PdfWriter
from PyPDF2.generic import TextStringObject, NumberObject
from django.views import View
from users.models import Student, Teacher
from datetime import datetime
import os
from django.conf import settings

# Create your views here.


def generate_bonafide():
    pass


class GenerateBonafideView(View):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        student: Student = request.user.student
        hod: Teacher = Teacher.objects.get(post="HOD")

        student_name = (
            student.first_name + " " + student.fathers_name + " " + student.last_name
        )
        fathers_name = student.fathers_name + " " + student.last_name
        ctime = datetime.now().strftime("%d/%m/%Y")

        template_path = "assets/bonafide_template.pdf"
        template_pdf = PdfReader(template_path)
        output = PdfWriter()

        page = template_pdf.pages[0]
        field1 = page["/Annots"][1].get_object()
        field1.update(
            {
                TextStringObject("/V"): TextStringObject(student_name),
                TextStringObject("/AP"): TextStringObject(""),
                TextStringObject("/AS"): TextStringObject("/Off"),
                TextStringObject("/Ff"): NumberObject(1),
            }
        )
        field2 = page["/Annots"][2].get_object()
        field2.update(
            {
                TextStringObject("/V"): TextStringObject(fathers_name),
                TextStringObject("/AP"): TextStringObject(""),
                TextStringObject("/AS"): TextStringObject("/Off"),
                TextStringObject("/Ff"): NumberObject(1),
            }
        )
        field3 = page["/Annots"][3].get_object()
        field3.update(
            {
                TextStringObject("/V"): TextStringObject(ctime),
                TextStringObject("/AP"): TextStringObject(""),
                TextStringObject("/AS"): TextStringObject("/Off"),
                TextStringObject("/Ff"): NumberObject(1),
            }
        )
        field4 = page["/Annots"][4].get_object()
        field4.update(
            {
                TextStringObject("/V"): TextStringObject(
                    str(student.semester) + " semester"
                ),
                TextStringObject("/AP"): TextStringObject(""),
                TextStringObject("/AS"): TextStringObject("/Off"),
                TextStringObject("/Ff"): NumberObject(1),
            }
        )

        if student.branch == "CO":
            branch = "Computer Engineering"
        elif student.branch == "ET":
            branch = "Electronics and Telecommunication Engineering"
        elif student.branch == "EE":
            branch = "Electrical Engineering"
        elif student.branch == "ME":
            branch = "Mechanical Engineering"
        else:
            branch = "Civil Engineering"

        field5 = page["/Annots"][5].get_object()
        field5.update(
            {
                TextStringObject("/V"): TextStringObject(branch),
                TextStringObject("/AP"): TextStringObject(""),
                TextStringObject("/AS"): TextStringObject("/Off"),
                TextStringObject("/Ff"): NumberObject(1),
            }
        )

        if student.semester % 2 == 0:
            year = f"{datetime.now().year-1}-{datetime.now().year}"
        else:
            year = f"{datetime.now().year}-{datetime.now().year+1}"

        field6 = page["/Annots"][6].get_object()
        field6.update(
            {
                TextStringObject("/V"): TextStringObject(year),
                TextStringObject("/AP"): TextStringObject(""),
                TextStringObject("/AS"): TextStringObject("/Off"),
                TextStringObject("/Ff"): NumberObject(1),
            }
        )

        field7 = page["/Annots"][7].get_object()
        field7.update(
            {
                TextStringObject("/V"): TextStringObject(f"GPK/{student.branch}/BONA/"),
                TextStringObject("/AP"): TextStringObject(""),
                TextStringObject("/AS"): TextStringObject("/Off"),
                TextStringObject("/Ff"): NumberObject(1),
            }
        )
        field8 = page["/Annots"][8].get_object()
        field8.update(
            {
                TextStringObject("/V"): TextStringObject(
                    hod.first_name + " " + hod.last_name
                ),
                TextStringObject("/AP"): TextStringObject(""),
                TextStringObject("/AS"): TextStringObject("/Off"),
                TextStringObject("/Ff"): NumberObject(1),
            }
        )

        output.add_page(page)

        dowload_url = os.path.join(
            settings.STATICFILES_DIRS[0],
            "downloads",
            "bonafides",
            f"bonafide_{student.enrollment_number}.pdf",
        )

        with open(dowload_url, "wb") as output_file:
            output.write(output_file)

        response = FileResponse(
            open(dowload_url, "rb"), content_type="application/pdf", as_attachment=True
        )

        return response
