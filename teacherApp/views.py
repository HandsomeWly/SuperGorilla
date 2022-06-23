import json

import pymysql
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

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
    tno=request.GET.get('tno')
    cname=request.GET.get('cname');
    cdate=request.GET.get('cdate');
    tname = request.GET.get('tname');
    credit = request.GET.get('credit');
    desc= request.GET.get('desc');
    max=request.GET.get('max');
    cposition = request.GET.get('cposition');
    print(tno);
    if(cposition==None):
        cposition=''

    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='rainng_course')
    cursor = conn.cursor()

    sql=("select * from course")
    cursor.execute(sql)
    course_num=cursor.fetchall()
    print(len(course_num),"***")
    sql=("SELECT teacher.teacher_id from teacher where teacher_number="+tno)
    cursor.execute(sql)
    teaID=cursor.fetchone()
    print(teaID[0])
    c='"'
    d=','
    e='","'

    sql = ("insert into course(course_name,course_teacher_id,course_credit,course_date,course_location,course_selected_count) " +
                'value(' +c+cname+e+str(teaID[0])+e+ credit+e+cdate+e+cposition+e+max+c+')' )
    print(sql)
    cursor.execute(str(sql))
    conn.commit()
    sql = ("select * from course")
    cursor.execute(sql)
    course_num = cursor.fetchall()
    print(course_num)
    return HttpResponse('yes')


def set_homework(request):
    courseID=request.GET.get('course')
    coursePutin=request.GET.get('putin')
    selectform = models.course_selection.objects.filter(course__cnb=courseID)
    course=models.course.objects.filter()
    print(course)
    for line in selectform:
        print(line.student.email)
    print(len(selectform))
    for line in selectform:
        task=models.Task()
        task.Stunmb=line.student
        task.putin=coursePutin
        task.course=course[0]
        task.evaluate=0
        print(task)
        task.save()
    print(len(models.Task.objects.all()))
    req={
        'msg':"1"
    }
    return JsonResponse(req)

@csrf_exempt
def teacherLogin(request):
    Ttunmb = request.GET.get('teacherID')
    password = request.GET.get('password')
    if(Ttunmb == None and password == None):
        Ttunmb = request.POST.get('teacherID')
        password = request.POST.get('password')
    if_success=0
    error=0
    teachers = models.Teacher.objects.all()
    if_Stunumber_exists=0
    for teacher in teachers:
        if(Ttunmb==teacher.Ttunmb):
            if_Stunumber_exists=1
            if(password==teacher.password):
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
def change_course_Date(request):
    cname=request.GET.get('cname')
    cdate=request.GET.get('cdate')
    print(cname,cdate)
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='rainng_course')
    cursor = conn.cursor()
    sql=('UPDATE course set course.course_date="{}" '.format(cdate)+
    'where course_name="{}"'.format(cname))
    print(sql)
    cursor.execute(str(sql))
    conn.commit()
    return HttpResponse("yes");

@csrf_exempt
def change_course_Position(request):
    cname=request.GET.get('cname')
    cposition=request.GET.get('cposition')
    print(cname,cposition)
    if(cposition==None):
        cposition=''
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='rainng_course')
    cursor = conn.cursor()
    sql=('UPDATE course set course_location="{}" '.format(cposition)+
    'where course_name="{}"'.format(cname))
    print(sql)
    cursor.execute(str(sql))
    conn.commit()
    return HttpResponse("yes");

@csrf_exempt
def delete_Course(request):
    cname=request.GET.get('cname');
    print(cname)
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='rainng_course')
    cursor = conn.cursor()
    sql=('delete from course where course.course_name="{}"'.format(cname))
    print(sql)
    cursor.execute(sql)
    conn.commit()
    return HttpResponse("yes")