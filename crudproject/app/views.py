import http, io, json
from django.shortcuts import render
from requests import request
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
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
    
    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data = python_data)
        if serializer.is_valid():
            serializer.save()
            msg = {'message':"Data created"}
            json_data = JSONRenderer().render(msg)
            # json_data = json.dumps(msg)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')



