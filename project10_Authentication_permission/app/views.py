from requests import Session
from .models import Student
from.serializers import StudentSerializer, serializers
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny, \
    IsAuthenticatedOrReadOnly, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly


#this Provides Read-only operations to perform
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    #AUTH AND PERMISSION for Class View
    # authentication_classes = [BasicAuthentication]
    authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated]

    #ISADMIN USER: IF is_staff:True then can use this API
    # permission_classes = [IsAdminUser]

    # permission_classes = [IsAuthenticatedOrReadOnly]
    # permission_classes = [DjangoModelPermissions]

    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]