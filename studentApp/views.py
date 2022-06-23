import json
import os

import pymysql
from django.http import HttpResponse, JsonResponse, FileResponse, StreamingHttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from studentApp import models, tests
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
    Stunmb = request.GET.get('Stunmb')
    password = request.GET.get('password')
    email = request.GET.get('email')
    school = request.GET.get('school')
    print(Stunmb,email,password)
    error_number=0
    students = models.Student.objects.all()
    for student in students:
        if student.Stunmb==Stunmb:
            error_number=1


    stu=Student()
    stu.Stunmb=Stunmb
    stu.password = password
    stu.email = email

    if error_number!=1:
        stu.save()
        student_queryset = models.Student.objects.all()
        if(len(student_queryset)== len(students)):
            error_number=2
    res={
        'err':error_number
    }
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='rainng_course')
    cursor = conn.cursor()
    sql=('INSERT INTO student(student_number,student_email,student_password,student_school) '+
        'values("{}","{}","{}","{}")'.format(Stunmb,email,password,school))
    if(error_number==0):
        print(sql)
        cursor.execute(sql)
        conn.commit()
    print(res)
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
    coursename=request.GET.get('coursename')
    stunum=request.GET.get('stunum')
    print(coursename)
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='rainng_course')
    cursor = conn.cursor()
    print(coursename)
    sql=("select student_id from student where student_number={}".format(stunum))
    print(sql)
    cursor.execute(sql)
    stuid=cursor.fetchone()
    print(stuid[0])
    stuid=stuid[0]

    sql = ('select course_id from course where course_name="{}"'.format(coursename))
    cursor.execute(sql)
    cid = cursor.fetchone()
    print(cid[0])
    cid=cid[0]

    sql = ('select * from sc')
    cursor.execute(sql)
    sclist=cursor.fetchall()

    msg=""
    for sc in sclist:
        if(sc[1]==stuid and sc[2]==cid):
            msg="repeat"
    if(msg!="repeat"):
        sql=('INSERT INTO sc(sc_student_id,sc_course_id,sc_score) '
            'values({},{},0) '.format(stuid,cid))
        print(sql)
        cursor.execute(sql)
        conn.commit()
        msg="yes"

    return HttpResponse(msg)

@csrf_exempt
def deleteCourseInfo(request):
    coursename = request.GET.get('coursename')
    stunum = request.GET.get('stunum')
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='rainng_course')
    cursor = conn.cursor()
    sql=('DELETE FROM sc '
        'where sc.sc_student_id=(select student.student_id from student where student_number="{}") '
        'and sc_course_id=(select course.course_id from course where course_name="{}")').format(stunum,coursename)
    print(sql)
    cursor.execute(sql)
    conn.commit()
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
        path="material/images/selfLogo/"+name
        file = open(path, "rb")

    return HttpResponse(file.read(), content_type='image/jpg')


@csrf_exempt
def upload_picture(request,stunum=None):
    filename=stunum+'.jpg'
    obj = request.FILES.get('file')
    print(obj)
    print(obj, '**', type(obj), obj.name)
    import os
    file_path = os.path.join('material/images/selfLogo/', filename)
    f = open(file_path, mode="wb")
    for i in obj.chunks():
        f.write(i)
    f.close()
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='rainng_course')
    cursor = conn.cursor()
    sql = ('insert into stuplus(student_number,logoFile) values("{}","selfLogo/{}") '.format(stunum,filename) +
           'ON DUPLICATE KEY UPDATE logoFile = "selfLogo/{}"'.format(filename))
    print(sql)
    cursor.execute(sql)
    conn.commit()

    return HttpResponse('yes')



@csrf_exempt
def example_Document(request):
    path = "material/documents/miaoshu.txt"
    file_one = open(path, "rb")
    return FileResponse(file_one.read().decode(encoding='utf-8'), content_type='octet-stream',filename='miaoshu.txt')


@csrf_exempt
def getTheDocument(request,cname=None):
    print(cname)
    import studentApp.tests
    tests.mkdir(cname)
    obj = request.FILES.get('file')
    print(obj)
    print(obj,'**', type(obj), obj.name)
    import os
    file_path = os.path.join('material/documents/'+cname, obj.name)
    f = open(file_path, mode="wb")
    for i in obj.chunks():
        f.write(i)
    f.close()
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='rainng_course')
    cursor = conn.cursor()
    sql=('INSERT into file values("{}","{}")'.format(cname,obj.name))
    print(sql)
    cursor.execute(sql)
    conn.commit()

    return HttpResponse('yes')

@csrf_exempt
def downloadfile(request, cname=None, filename=None):
    print(cname,filename)
    response = FileResponse(open("material/documents/{}/{}".format(cname,filename), "rb"),filename=filename)
    response['Content-Type'] ="application/octet-stream"
    response['Content-Disposition'] = 'attachment;filename="{}"'.format(filename)
    return response



