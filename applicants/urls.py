from .views import ApplicantApi
from django.urls import path

urlpatterns = [
    path(
        "applicant-list-api/",
        ApplicantApi.as_view({"get": "list"}),
        name="applicant-list-api",
    ),
    path(
        "applicant-create-api/",
        ApplicantApi.as_view({"post": "create"}),
        name="applicant-create-api",
    ),
    path(
        "applicant-retrieve-api/<id>",
        ApplicantApi.as_view({"get": "retrieve"}),
        name="applicant-retrieve-api",
    ),
]
