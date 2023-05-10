from django.urls import path
from .views import GenerateSingleTcView, TcDetailsView

app_name = "tc"

urlpatterns = [
    path("single/", GenerateSingleTcView.as_view(), name="single-tc"),
    path("get-details/<int:pk>", TcDetailsView.as_view(), name="tc-details"),
]
