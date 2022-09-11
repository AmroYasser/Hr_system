from .models import Applicant
from rest_framework import serializers


class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = [
            "id",
            "full_name",
            "date_of_birth",
            "years_of_experince",
            "department_id",
            "resume",
        ]
