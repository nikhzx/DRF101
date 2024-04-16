from .models import Student
from.serializers import StudentSerializer, serializers
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny


#this Provides Read-only operations to perform
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    #AUTH AND PERMISSION for Class View
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]

    #ISADMIN USER: for he user who have is_staff:True and use this API
    # permission_classes = [IsAdminUser]