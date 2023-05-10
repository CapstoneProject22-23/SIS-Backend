from django.shortcuts import render, get_object_or_404
from django.views import View
import pdfrw
from django.http import HttpResponse
from PyPDF2.generic import TextStringObject, NumberObject
from PyPDF2 import PdfReader, PdfWriter
from rest_framework.views import APIView, Response
import os
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from rest_framework import permissions
from users.models import Student
from rest_framework.generics import RetrieveAPIView
from django.conf import settings

# Create your views here.


@method_decorator(staff_member_required, name="dispatch")
class TcDetailsView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, pk):
        student = Student.objects.get(pk=pk)

        response = {
            "enrollment_number": pk,
            "full_name": student.first_name
            + " "
            + student.fathers_name
            + " "
            + student.last_name,
            "mother_name": student.mothers_name,
            "religion": "------",
            "category": student.category,
            "sub_cat": student.sub_category,
            "nationality": "indian",
            "birth_place": student.birth_place,
            "dob": student.dob,
        }

        return Response(response)


@method_decorator(staff_member_required, name="dispatch")
class GenerateSingleTcView(APIView):
    def post(self, request):
        student_name = request.POST.get("name")  # Rplace with your actual data
        enrollment_number = request.POST.get(
            "enrollment_number"
        )  # Replace with your actual data
        mother_name = request.POST.get("mothers_name")
        religion = request.POST.get("religion")
        category = request.POST.get("category")
        birth_place = request.POST.get("birth_place")
        dob = request.POST.get("dob")
        dob_words = request.POST.get("dob_words")
        prior = request.POST.get("prior")
        admission_date = request.POST.get("admission_date")
        reason = request.POST.get("reason")
        conduct = request.POST.get("conduct")
        remarks = request.POST.get("remarks")
        date = request.POST.get("date")

        # student = get_object_or_404(Student, enrollment_number=enrollment_number)
        # Load the TC template
        template_path = "assets/tc_template_1.pdf"
        template_pdf = PdfReader(template_path)
        output = PdfWriter()

        page = template_pdf.pages[0]

        # print(page['/Annots'][0].get_object())
        # print(page['/Annots'][1].get_object())
        field1 = page["/Annots"][0].get_object()
        field1.update(
            {
                TextStringObject("/V"): TextStringObject("0021"),
                TextStringObject("/AP"): TextStringObject(""),
                TextStringObject("/AS"): TextStringObject("/Off"),
                TextStringObject("/Ff"): NumberObject(1),
            }
        )
        field2 = page["/Annots"][1].get_object()
        field2.update(
            {
                TextStringObject("/V"): TextStringObject(enrollment_number),
                TextStringObject("/AP"): TextStringObject(""),
                TextStringObject("/AS"): TextStringObject("/Off"),
                TextStringObject("/Ff"): NumberObject(1),
            }
        )
        field3 = page["/Annots"][2].get_object()
        field3.update(
            {
                TextStringObject("/V"): TextStringObject(student_name),
                TextStringObject("/AP"): TextStringObject(""),
                TextStringObject("/AS"): TextStringObject("/Off"),
                TextStringObject("/Ff"): NumberObject(1),
            }
        )
        field4 = page["/Annots"][3].get_object()
        field4.update(
            {
                TextStringObject("/V"): TextStringObject(mother_name),
                TextStringObject("/AP"): TextStringObject(""),
                TextStringObject("/AS"): TextStringObject("/Off"),
                TextStringObject("/Ff"): NumberObject(1),
            }
        )
        field5 = page["/Annots"][4].get_object()
        field5.update(
            {
                TextStringObject("/V"): TextStringObject(religion),
                TextStringObject("/AP"): TextStringObject(""),
                TextStringObject("/AS"): TextStringObject("/Off"),
                TextStringObject("/Ff"): NumberObject(1),
            }
        )
        field6 = page["/Annots"][5].get_object()
        field6.update(
            {
                TextStringObject("/V"): TextStringObject(category),
                TextStringObject("/AP"): TextStringObject(""),
                TextStringObject("/AS"): TextStringObject("/Off"),
                TextStringObject("/Ff"): NumberObject(1),
            }
        )
        field7 = page["/Annots"][6].get_object()
        field7.update(
            {
                TextStringObject("/V"): TextStringObject("Indian"),
                TextStringObject("/AP"): TextStringObject(""),
                TextStringObject("/AS"): TextStringObject("/Off"),
                TextStringObject("/Ff"): NumberObject(1),
            }
        )
        field8 = page["/Annots"][7].get_object()
        field8.update(
            {
                TextStringObject("/V"): TextStringObject(birth_place),
                TextStringObject("/AP"): TextStringObject(""),
                TextStringObject("/AS"): TextStringObject("/Off"),
                TextStringObject("/Ff"): NumberObject(1),
            }
        )
        field9 = page["/Annots"][8].get_object()
        field9.update(
            {
                TextStringObject("/V"): TextStringObject(dob),
                TextStringObject("/AP"): TextStringObject(""),
                TextStringObject("/AS"): TextStringObject("/Off"),
                TextStringObject("/Ff"): NumberObject(1),
            }
        )
        field10 = page["/Annots"][9].get_object()
        field10.update(
            {
                TextStringObject("/V"): TextStringObject(dob_words),
                TextStringObject("/AP"): TextStringObject(""),
                TextStringObject("/AS"): TextStringObject("/Off"),
                TextStringObject("/Ff"): NumberObject(1),
            }
        )
        field11 = page["/Annots"][10].get_object()
        field11.update(
            {
                TextStringObject("/V"): TextStringObject(prior),
                TextStringObject("/AP"): TextStringObject(""),
                TextStringObject("/AS"): TextStringObject("/Off"),
                TextStringObject("/Ff"): NumberObject(1),
            }
        )
        field12 = page["/Annots"][11].get_object()
        field12.update(
            {
                TextStringObject("/V"): TextStringObject(admission_date),
                TextStringObject("/AP"): TextStringObject(""),
                TextStringObject("/AS"): TextStringObject("/Off"),
                TextStringObject("/Ff"): NumberObject(1),
            }
        )
        field13 = page["/Annots"][12].get_object()
        field13.update(
            {
                TextStringObject("/V"): TextStringObject(reason),
                TextStringObject("/AP"): TextStringObject(""),
                TextStringObject("/AS"): TextStringObject("/Off"),
                TextStringObject("/Ff"): NumberObject(1),
            }
        )
        field14 = page["/Annots"][13].get_object()
        field14.update(
            {
                TextStringObject("/V"): TextStringObject(conduct),
                TextStringObject("/AP"): TextStringObject(""),
                TextStringObject("/AS"): TextStringObject("/Off"),
                TextStringObject("/Ff"): NumberObject(1),
            }
        )
        field15 = page["/Annots"][14].get_object()
        field15.update(
            {
                TextStringObject("/V"): TextStringObject(remarks),
                TextStringObject("/AP"): TextStringObject(""),
                TextStringObject("/AS"): TextStringObject("/Off"),
                TextStringObject("/Ff"): NumberObject(1),
            }
        )
        field16 = page["/Annots"][15].get_object()
        field16.update(
            {
                TextStringObject("/V"): TextStringObject(date),
                TextStringObject("/AP"): TextStringObject(""),
                TextStringObject("/AS"): TextStringObject("/Off"),
                TextStringObject("/Ff"): NumberObject(1),
            }
        )
        print(page["/Annots"][0].get_object())
        output.add_page(page)

        download_url = os.path.join(
            settings.STATICFILES_DIRS[0],
            "downloads",
            "tcs",
            f"tc_{enrollment_number}.pdf",
        )

        with open(download_url, "wb") as output_file:
            output.write(output_file)

        if os.path.exists(download_url):
            # Create the download URL
            download_link = (
                "http://localhost:8000/"
                + settings.STATIC_URL
                + f"downloads/tc_{enrollment_number}.pdf"
            )
            # Construct the response with the download URL
            response_data = {
                "download_url": download_link,
            }
            return Response(response_data)

        # If the file doesn't exist, return a 404 response
        return Response({"detail": "TC PDF not found."}, status=404)
