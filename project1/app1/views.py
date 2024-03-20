from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse

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