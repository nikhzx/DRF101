from functools import partial
import http, io, json
from django.shortcuts import render
from django.views import View
from requests import request
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

#Class Based View
@method_decorator(csrf_exempt, name = 'dispatch') #When you use @method_decorator(csrf_exempt, name='dispatch'), it means that the csrf_exempt decorator should be applied to the dispatch method of the class-based view.The dispatch method in Django class-based views is responsible for routing incoming HTTP requests to the appropriate method (e.g., get, post, put, delete, etc.) based on the HTTP method used in the request. By applying csrf_exempt decorator to the dispatch method, you are exempting the view from CSRF (Cross-Site Request Forgery) protection.
class StudentAPI(View):
    def get(self, request, *args, **kwargs):
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

    def post(self, request, *args, **kwargs):
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
        
    def put(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=python_data, partial=True) #Here partial = True is used for partial modification
        if serializer.is_valid():
            serializer.save()
            msg = {'message':'Data Updated'}
            jsondata = JSONRenderer().render(msg)
            return HttpResponse(jsondata, content_type = 'application/json')
        jsondata = JSONRenderer().render(serializer.errors)
        return HttpResponse(jsondata, content_type = 'application/json') 
    
    def delete(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)  
        python_data = JSONParser().parse(stream)
        id = python_data.get("id", None)
        # for i in id:
        #     stu = Student.objects.get(id=i)
        #     stu.delete()
        stu = Student.objects.get(id=id)
        stu.delete()
        msg = {'msg':"Data Deleted"}
        return JsonResponse(msg)

#function based views - Commented for Learning Class based
# @csrf_exempt
# def student_api(request):
#     if request.method == "GET":
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)
#         id = python_data.get('id', None)
#         if id is not None :
#             data = Student.objects.get(id = id)
#             serializer = StudentSerializer(data)
#             json_data = JSONRenderer().render(serializer.data)
#             return HttpResponse(json_data, content_type = 'application/json')
#         else:  
#             data = Student.objects.all()
#             serializer = StudentSerializer(data, many = True)
#             json_data = JSONRenderer().render(serializer.data)
#             return HttpResponse(json_data, content_type = "application/json")
    
#     if request.method == "POST":
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)
#         serializer = StudentSerializer(data = python_data)
#         if serializer.is_valid():
#             serializer.save()
#             msg = {'message':"Data created"}
#             json_data = JSONRenderer().render(msg)
#             # json_data = json.dumps(msg)
#             return HttpResponse(json_data, content_type='application/json')
#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data, content_type='application/json')
    
#     if request.method == "PUT":
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)
#         id = python_data.get('id')
#         stu = Student.objects.get(id=id)
#         serializer = StudentSerializer(stu, data=python_data, partial=True) #Here partial = True is used for partial modification
#         if serializer.is_valid():
#             serializer.save()
#             msg = {'message':'Data Updated'}
#             jsondata = JSONRenderer().render(msg)
#             return HttpResponse(jsondata, content_type = 'application/json')
#         jsondata = JSONRenderer().render(serializer.errors)
#         return HttpResponse(jsondata, content_type = 'application/json')  

#     if request.method == "DELETE":
#         json_data = request.body
#         stream = io.BytesIO(json_data)  
#         python_data = JSONParser().parse(stream)
#         id = python_data.get("id", None)
#         stu = Student.objects.get(id=id)
#         stu.delete()
#         msg = {'msg':"Data Deleted"}
#         return JsonResponse(msg)