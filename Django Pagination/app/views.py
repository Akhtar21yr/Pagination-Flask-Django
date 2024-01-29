from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer
from django.core.paginator import Paginator

class StudentView(APIView):
    def get(self, request, rollno=None):

        if rollno:
            student = get_object_or_404(Student, rollno=rollno)
            serializer = StudentSerializer(student)
            return Response({'student': serializer.data}, status=status.HTTP_200_OK)
        else:
            students = Student.objects.all()
            page_no = request.query_params.get('page', 1) # getting the page no from params
            item_per_page = request.query_params.get('count', 4) # getting no. of row 
            paginator = Paginator(students, item_per_page) # creating paginator object
            page_object = paginator.get_page(page_no) # geting the page 
            serializer = StudentSerializer(page_object.object_list, many=True) #serializing the list of dta
            return Response({'students': serializer.data}, status=status.HTTP_200_OK) # returting the data 

    

    def post(self, request):
        data = request.data
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Student created successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, rollno):
        student = get_object_or_404(Student, rollno=rollno)
        data = request.data
        serializer = StudentSerializer(student, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Student updated successfully'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, rollno):
        student = get_object_or_404(Student, rollno=rollno)
        data = request.data
        serializer = StudentSerializer(student, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Student updated successfully'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
