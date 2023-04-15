from django.shortcuts import render
from django.contrib.auth import login
from rest_framework.views import APIView
from knox.views import LoginView as KnoxLoginView
from django.http import FileResponse
from rest_framework import generics, permissions
from reportlab.pdfgen.canvas import Canvas
import io
from reportlab.lib.units import mm, inch
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader
from PIL import Image

"""

class LoginView(View):
    def get(self, request):
        pass
    
    def post(self, request):
        pass
        
"""

# Create your views here.
from .serializers import CustomUserSerializer, AuthTokenSerializer


class CreateUserView(generics.CreateAPIView):
    serializer_class = CustomUserSerializer


class LoginView(KnoxLoginView):
    # serializer_class = LoginSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']  # type:ignore

        login(request, user)

        return super(LoginView, self).post(request, format=None)


class ManageUserView(generics.RetrieveAPIView):
    serializer_class = CustomUserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user


class TCView(APIView):

    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        buffer = io.BytesIO()
        image = ImageReader('./assets/TC_TEMPLATE.jpg')

        PAGE_WIDTH, PAGE_HEIGHT = letter

    # Create PDF canvas
        pdf_canvas = Canvas(buffer, pagesize=letter)

        pdf_canvas.drawImage(
            image, x=0, y=0, width=PAGE_WIDTH, height=PAGE_HEIGHT)

        pdf_canvas.drawString(1 * inch, 10 * inch, "hello World")

        pdf_canvas.save()

        buffer.seek(0)
        return FileResponse(buffer, as_attachment=True, filename='output.pdf')
