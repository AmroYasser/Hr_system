from django.db import models
from django.core.exceptions import ValidationError
import os

DEPARTMENT_CHOICES = [
    ("IT", "IT"),
    ("HR", "HR"),
    ("FIN", "Finance"),
]


class Applicant(models.Model):
    full_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    years_of_experince = models.DecimalField(max_digits=4, decimal_places=2)
    regestration_date = models.DateTimeField(auto_now_add=True)
    department_id = models.CharField(
        max_length=3, choices=DEPARTMENT_CHOICES, default="IT"
    )

    def validate_file_extension(value):
        ext = os.path.splitext(value.name)[1]
        valid_extensions = [".pdf", ".docx"]
        if not ext in valid_extensions:
            raise ValidationError("File not supported!")

    resume = models.FileField(upload_to="resumes", validators=[validate_file_extension])
