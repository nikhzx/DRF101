from functools import partial
from .models import Student
from .serializers import StudentSerializer
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

#Function Based api_view
@api_view(['GET', 'POST']) #GET is not necessary to include here, its Auto Included
def main_function(request):
    if request.method == "GET":
        return Response({'msg':"This is GET Request"})
    
    if request.method == "POST":
        print(request.data)
        return Response({'msg':"This is POST Request"})

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def student_api(request):
    if request.method == 'GET':
        id = request.data.get('id') #get the id value from request.data obj | very simple compare to previous 
        if id is not None:
            stu = Student.objects.get(id=id) #Model Object
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)
    
    if request.method=='POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"Data Created"})
        return Response(serializer.errors)
    
    if request.method=='PUT':
        id = request.data.get('id')
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated'})
        return Response(serializer.errors)
    
    if request.method == 'DELETE':
        id = request.data.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        return Response({'msg':f'(Data Deleted for id:{id})'})