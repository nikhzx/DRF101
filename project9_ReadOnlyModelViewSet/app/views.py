from .models import Student
from.serializers import StudentSerializer, serializers
from rest_framework import viewsets

#this Provides Read-only operations to perform
class StudentModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer