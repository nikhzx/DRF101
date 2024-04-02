from rest_framework import serializers
from .models import Student

#Model Serializer
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'roll', 'city']

        