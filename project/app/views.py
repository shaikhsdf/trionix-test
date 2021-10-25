from django.shortcuts import render
from .models import student
from . import models
from .constants import *
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from .serializers import StudentSerializer

@csrf_exempt
def studentApi(request,id=0):
    if request.method=='GET':
        students = getattr(models, STUDENT).objects.all()
        students_serializer=StudentSerializer(students,many=True)
        return JsonResponse(students_serializer.data,safe=False)
    elif request.method=='POST':
        student_data=JSONParser().parse(request)
        students_serializer=StudentSerializer(data=student_data)
        if students_serializer.is_valid():
            students_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        student_data=JSONParser().parse(request)
        student=getattr(models, STUDENT).objects.get(StudentId=student_data['StudentId'])
        students_serializer=StudentSerializer(student,data=student_data)
        if students_serializer.is_valid():
            students_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        student=getattr(models, STUDENT).objects.get(StudentId=id)
        student.delete()
        return JsonResponse("Deleted Successfully",safe=False)



def create(request):
    first_name = request.POST.get(FIRST_NAME)
    last_name = request.POST.get(LAST_NAME)
    dob = request.POST.get(DOB)
    email = request.POST.get(EMAIL)
    gender = request.POST.get(GENDER)

    try:
        getattr(models, STUDENT).objects.get(**{EMAIL: email})
        return HttpResponse("Student Email ID Already Exist")
    except Exception as ex:
        print(ex)
        getattr(models, STUDENT).objects.create(**{
            FIRST_NAME: first_name,
            LAST_NAME: last_name,
            DOB: dob,
            EMAIL: email,
            GENDER: gender
        })
        return HttpResponse("Student Created Sucessfully")

def edit(request, id):
    first_name = request.POST.get(FIRST_NAME)
    last_name = request.POST.get(LAST_NAME)
    dob = request.POST.get(DOB)
    email = request.POST.get(EMAIL)
    gender = request.POST.get(GENDER)

    try:
        getattr(models, STUDENT).objects.get(**{EMAIL: email}).exclude(**{PK: id})
        return HttpResponse("Student Email ID Already Exist")
    except Exception as ex:
        try:
            record = getattr(models, STUDENT).objects.get(**{PK: id})
            record.update(**{
                FIRST_NAME: first_name,
                LAST_NAME: last_name,
                DOB: dob,
                EMAIL: email,
                GENDER: gender
            })
            return HttpResponse("Student Data Updated")
        except Exception as ex:
            print(ex)
            return HttpResponse("Student Does Not Exist")
            
def delete(request, id):
    try:
        getattr(models, STUDENT).objects.get(**{PK: id})
        return HttpResponse("Student Data Deleted.")
    except Exception as ex:       
        print(ex)
        return HttpResponse("Student Does Not Exist")