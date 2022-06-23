import json
import os

import pymysql
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from studentApp import models
from studentApp.models import Student
from teacherApp.models import Teacher

@csrf_exempt
def courseInformation(request):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='rainng_course')
    cursor = conn.cursor()
    cursor.execute("select * from course inner join teacher on course.course_teacher_id=teacher.teacher_id")
    course_list = cursor.fetchall()
    list=[]
    j=0
    print(len(course_list))
    for course in course_list:
        list.append({
            'cname' : course[2],
            'grade':course[3],
            'time':course[11],
            'ccredit':course[6],
            'cposition': course[5],
            'tea':course[15]
        })
        j=j+1
    print(j)
    return JsonResponse(list, safe=False)
    #return HttpResponse(json.dumps(courses), content_type='application/json')

@csrf_exempt
def self_class_Info(request,username=None):
    #stunmb=request.POST.get('usrname')
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='rainng_course')
    cursor = conn.cursor()
    sql=("SELECT sc.sc_course_id ,course.course_name "+
    "from student inner join sc on student.student_id=sc.sc_student_id "+
    "inner join course on sc.sc_course_id=course.course_id "+
    "where student.student_number={}".format(username))
    print(sql)
    cursor.execute(sql)
    course_list = cursor.fetchall()
    list=[]
    for course in course_list:
        list.append({
            'cnb':course[0],
            'cname':course[1]
        })

    return JsonResponse(list, safe=False)


@csrf_exempt
def fileList(request,cname=None):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='rainng_course')
    cursor = conn.cursor()
    sql = ('select cname,file from file inner join course on file.cname=course.course_name '+
            'where cname="{}"'.format(cname))
    print(sql)
    cursor.execute(sql)
    filelist=cursor.fetchall()
    print(filelist)
    list=[]
    for file in filelist:
        list.append({
            'filename':file[1]
        })
    return JsonResponse(list, safe=False)


@csrf_exempt
def delete_file(request):
    cname = request.GET.get('cname')
    filename = request.GET.get('filename')
    print(cname,filename)

    import os
    os.remove("material/documents/{}/{}".format(cname,filename))

    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='rainng_course')
    cursor = conn.cursor()
    sql=('delete from file where cname="{}"and file="{}"'.format(cname,filename))
    cursor.execute(sql)
    conn.commit()

    return HttpResponse("yes")



@csrf_exempt
def studen_Info(request,username=None):

    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='rainng_course')
    cursor = conn.cursor()
    sql=('select * from student left join stuplus on student.student_number=stuplus.student_number where student.student_number={}'.format(username))
    print(sql)
    cursor.execute(sql)
    student=cursor.fetchone()
    print(student)
    return JsonResponse(student, safe=False)


@csrf_exempt
def change_student_Info(request):
    data=request.GET.get('data')
    type=request.GET.get('type')
    stunum=request.GET.get('stunum')
    print(data,type,stunum)
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='rainng_course')
    cursor = conn.cursor()
    sql=('')
    if(type=='grade'):
        sql=('insert into stuplus(student_number,grade) VALUES("{}","{}") '.format(stunum,data)+
            'ON DUPLICATE KEY UPDATE grade="{}" '.format(data))
    elif(type=='position'):
        sql = ('insert into stuplus(student_number,position) VALUES("{}","{}") '.format(stunum, data) +
               'ON DUPLICATE KEY UPDATE position="{}" '.format(data))
    elif(type=='autograph'):
        sql = ('insert into stuplus(student_number,autograph) VALUES("{}","{}") '.format(stunum, data) +
               'ON DUPLICATE KEY UPDATE autograph="{}" '.format(data))
    elif(type == 'name'):
        sql=('update student set student.student_name="{}" where student.student_number="{}"'.format(data,stunum))

    cursor.execute(sql)
    conn.commit()

    return HttpResponse("yes")




'''SELECT rc_student_course.sc_course_id ,rc_course.course_name
from rc_student inner join rc_student_course on rc_student.student_id=rc_student_course.sc_student_id
inner join rc_course on rc_student_course.sc_course_id=rc_course.course_id
where rc_student.student_number="123"'''