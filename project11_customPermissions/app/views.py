from requests import Session
from .custompermissions import MyPermission
from .models import Student
from.serializers import StudentSerializer, serializers
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


#this Provides Read-only operations to perform
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    #AUTH AND PERMISSION for Class View
    authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]

    #CustomPermission
    permission_classes = [MyPermission]
