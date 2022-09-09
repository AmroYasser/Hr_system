from .models import Applicant
from .serializers import ApplicantSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.http import HttpResponse
import mimetypes


# Create your views here.


class ApplicantApi(viewsets.ViewSet):
    serializer_class = ApplicantSerializer
    queryset = Applicant.objects.all()

    def list(self, request):
        if request.META.get("HTTP_X_ADMIN"):
            queryset = Applicant.objects.all().order_by("-regestration_date")
            serializer = ApplicantSerializer(queryset, many=True)
            return Response(serializer.data)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    def create(self, request):
        serializer = ApplicantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, id):
        if request.META.get("HTTP_X_ADMIN"):
            obj = Applicant.objects.filter(id=id).first()

            response = HttpResponse(
                obj.resume, content_type=mimetypes.guess_type(obj.resume.name)[0]
            )
            return response
        return Response(status=status.HTTP_401_UNAUTHORIZED)
