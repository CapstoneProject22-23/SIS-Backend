from django.urls import path, include
from .views import ResultViewSet, RetrieveResultsView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"upload", ResultViewSet)

app_name = "result"

urlpatterns = [
    path("", include(router.urls)),
    path("retreive/", RetrieveResultsView.as_view(), name="retrieve-results"),
]
