from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import viewsets, status

class StudentViewSet(viewsets.ViewSet):
    def list(self, request):
        print("**************list***************")
        print("Basename:", self.basename)
        print("Action:", self.action)
        print("Detail:", self.detail)
        print("Suffix:", self.suffix)
        print("Name:", self.name)
        print("Description:", self.description)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many= True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        serilaizer = StudentSerializer(data=request.data)
        if serilaizer.is_valid():
            serilaizer.save()
            msg = {'msg':"Data Created"}
            return Response(msg, status=status.HTTP_201_CREATED)
        return Response(serilaizer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk):
        id=pk
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"Data Completely Updated!"}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, pk):
        id = pk
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"Data Partially Modified"}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk):
        id=pk
        stu = Student.objects.get(id=id)
        stu.delete()
        return Response({'msg':'DATA DELETED'})