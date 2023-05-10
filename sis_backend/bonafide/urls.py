from django.urls import path
from .views import GenerateBonafideView

app_name = "bonafide"

urlpatterns = [
    path("download/", GenerateBonafideView.as_view(), name="bonafide"),
]
