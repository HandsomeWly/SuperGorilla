import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from studentApp import models
from studentApp.models import Student


# Create your views here.
def index(request):
    data = {
        'account': '12345',
        'password': 'password',
    }
    return HttpResponse(json.dumps(data), content_type='application/json')

@csrf_exempt
def courseInformation(request):
    #students = models.Student.objects.all()
    courses=models.course.objects.values().filter()
    print(courses)
    course_list = list(courses)
    return JsonResponse(course_list, safe=False)

@csrf_exempt
def studentInformation(request):
    #students = models.Student.objects.all()
    students=models.Student.objects.values().filter()
    print(students)
    student_list = list(students)
    return JsonResponse(student_list, safe=False)

@csrf_exempt
def teacherInformation(request):
    #teachers = models.Teacher.objects.all()
    teachers=models.Teacher.objects.values().filter()
    print(teachers)
    teacher_list = list(teachers)
    return JsonResponse(teacher_list, safe=False)