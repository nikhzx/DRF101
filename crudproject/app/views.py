import http
from django.shortcuts import render
from requests import request
import io
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

# Create your views here.
def student_api(request):
    if request.method == "GET":
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id', None)
        if id is not None :
            data = Student.objects.get(id = id)
            serializer = StudentSerializer(data)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type = 'application/json')
        else:  
            data = Student.objects.all()
            serializer = StudentSerializer(data, many = True)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type = "application/json")
