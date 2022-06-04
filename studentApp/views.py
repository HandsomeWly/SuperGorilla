import json
import os

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from studentApp import models
from studentApp.models import Student
from teacherApp.models import Teacher


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
    email = request.POST['email']
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
    stu.email = email

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
    Stunmb = request.GET.get('Stunmb')
    password = request.GET.get('password')
    if(Stunmb == None and password == None):
        Stunmb = request.POST.get('Stunmb')
        password = request.POST.get('password')
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


@csrf_exempt
def courseInformation(request):
    #students = models.Student.objects.all()
    courses=models.course.objects.values().filter()
    print(courses)
    course_list = list(courses)
    return JsonResponse(course_list, safe=False)
    #return HttpResponse(json.dumps(courses), content_type='application/json')



@csrf_exempt
def courseSelect(request):
    courseInfo=models.course_selection()
    courseInfo.student_id=request.POST['student_id']
    courseInfo.course_id = request.POST['course_id']
    courseInfo.select_time=request.POST['select_time']
    courseInfo.grade=0
    courseInfo.save()
    '''courses=models.course_selection.objects.all()
    for course in courses:'''
    print()
    return HttpResponse("yes")


@csrf_exempt
def studentLoginUseAxois_Tmp(request):
    '''Stunmb = request.POST.get('Stunmb')
    password = request.POST.get('password')'''

    data=json.loads(request.body)
    Stunmb=data['Stunmb']
    password=data['password']
    print(Stunmb,password)
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



@csrf_exempt
def studentRegisterUseAxois_Tmp(request):
    data = json.loads(request.body)
    Stunmb = data['Stunmb']
    password = data['password']
    phonenb = data['phonenb']
    Sname  = data['Sname']
    School = data['School']

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
def example_Picture(request):
    path = "material/images/example.jpg"
    file_one = open(path, "rb")
    return HttpResponse(file_one.read(), content_type='image/jpg')


@csrf_exempt
def picture(request,name=None):
    file=None
    if(name):
        path="material/images/"+name
        file = open(path, "rb")
    return HttpResponse(file.read(), content_type='image/jpg')



@csrf_exempt
def example_Document(request):
    path = "material/documents/miaoshu.txt"
    file_one = open(path, "rb")
    return HttpResponse(file_one.read().decode(encoding='utf-8'), content_type='file/txt')

@csrf_exempt
def getTheDocument(request):
    obj = request.FILES.get('document')
    print(obj,'**', type(obj), obj.name)
    import os
    file_path = os.path.join('material/documents', obj.name)
    f = open(file_path, mode="wb")
    for i in obj.chunks():
        f.write(i)
    f.close()
    return HttpResponse('yes')
