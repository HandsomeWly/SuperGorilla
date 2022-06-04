import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from studentApp import models
from studentApp.models import course_selection, Student,course


# Create your views here.
def index(request):
    data = {
        'account': '12345',
        'password': 'password',
    }
    return HttpResponse(json.dumps(data), content_type='application/json')

def teacher_course_application(request):
    cnb=request.POST.get('cnb');
    date=request.POST.get('date');
    print(cnb);

    return HttpResponse('yes')


def set_homework(request):
    courseID=request.GET.get('course')
    coursePutin=request.GET.get('putin')



    selectform = models.course_selection.objects.filter()
    course=models.course.objects.filter()
    print(course[0].cname)
    for line in selectform:
        print(line.student.email)
    print(len(selectform))
    for line in selectform:
        task=models.Task()
        task.Stunmb=line.student
        task.putin=coursePutin
        task.course=course[0]
        print(task)
        task.save()
    print(len(models.Task.objects.all()))
    req={
        'msg':"1"
    }
    return JsonResponse(req)