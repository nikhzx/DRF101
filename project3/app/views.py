from functools import partial
from .models import Student
from .serializers import StudentSerializer
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

#Function Based api_view
@api_view(['GET', 'POST']) #GET is not necessary to include here, its Auto Included
def main_function(request):
    if request.method == "GET":
        return Response({'msg':"This is GET Request"})
    
    if request.method == "POST":
        print(request.data)
        return Response({'msg':"This is POST Request"})

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def student_api(request, pk=None):
    if request.method == 'GET':
        # id = request.data.get('id') #get the id value from request.data obj | very simple compare to previous 
        id = pk 
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
            return Response({'msg':"Data Created"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method=='PUT':
        # id = request.data.get('id')
        id = pk
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    if request.method=='PATCH':
        # id = request.data.get('id')
        id = pk
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data Updated'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
      
    if request.method == 'DELETE':
        # id = request.data.get('id')
        id = pk
        stu = Student.objects.get(id=id)
        stu.delete()
        return Response({'msg':f'(Data Deleted for id:{id})'}, status=status.HTTP_200_OK)