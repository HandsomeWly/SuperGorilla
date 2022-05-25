import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from studentApp import models
from studentApp.models import Student


def index(request):
    data = {
        'account': '12345',
        'password': 'password',
    }
    return HttpResponse(json.dumps(data), content_type='application/json')

@csrf_exempt
def studentRegister(request):
    Stunmb = request.POST['Stunmb']
    password = request.POST['password']
    phonenb = request.POST['phonenb']
    Sname  = request.POST['Sname']
    School = request.POST['School']

    error_number=0
    students = models.Student.objects.all()
    for student in students:
        if student.Stunmb==Stunmb:
            error_number=1


    stu=Student()
    stu.Stunmb=Stunmb
    stu.password = password
    stu.phonenb = phonenb
    stu.Sname = Sname
    stu.School= School
    if error_number!=1:
        stu.save()
        student_queryset = models.Student.objects.all()
        if(len(student_queryset)== len(students)):
            error_number=2
    res={
        'err':error_number
        }
    return HttpResponse(json.dumps(res), content_type='application/json')


@csrf_exempt
def studentLogin(request):
    Stunmb = request.POST['Stunmb']
    password = request.POST['password']
    if_success=0
    error=0
    students = models.Student.objects.all()
    if_Stunumber_exists=0
    for student in students:
        if(Stunmb==student.Stunmb):
            if_Stunumber_exists=1
            if(password==student.password):
                if_success=1
            else:
                error=2
    if(if_Stunumber_exists==0):error=1
    res={
        'if_success':if_success,
        'error':error
    }
    return HttpResponse(json.dumps(res), content_type='application/json')