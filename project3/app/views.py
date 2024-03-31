import re
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
    