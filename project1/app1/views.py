import io
from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

# Model Object - Single Student DATA
def student_detail(request, pk):
    stu = Student.objects.get(id=pk)
    serializer = StudentSerializer(stu)
    # data = JSONRenderer().render(serializer.data)
    # return HttpResponse(data, content_type = 'application/json')
    return JsonResponse(serializer.data)

#QuerySet - All Student Data
def students_details(request):
    stu = Student.objects.all()
    serializer = StudentSerializer(stu, many = True)
    # data = JSONRenderer().render(serializer.data)
    # return HttpResponse(data, content_type = 'application/json')
    return JsonResponse(serializer.data, safe= False)

#Create a new Entry
@csrf_exempt
def student_create(request):
    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data = python_data)

        #check is Serializer obj is valid
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Inserted/Created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type = 'application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type = 'application/json')