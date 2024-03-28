from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length = 100)

    
    def create(self, validated_data):
        '''
        This Function is used for POST request handelling.
        '''
        return Student.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        '''
        This Method is used for PUT request handelling.
        '''
        instance.name = validated_data.get('name', instance.name)
        instance.roll = validated_data.get('roll', instance.roll)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance