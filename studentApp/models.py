from django.db import models
from teacherApp.models import Teacher
# Create your models here.
class Student(models.Model):
    """学生表"""
    #Saccount = models.CharField(verbose_name="学生账号",max_length=255)
    password = models.CharField(verbose_name="密码", max_length=255)
    Stunmb = models.CharField(verbose_name="学号", max_length=255)
    phonenb = models.CharField(verbose_name="手机号", max_length=11)
    Sname = models.CharField(verbose_name="学生姓名", max_length=255)
    School = models.CharField(verbose_name="学校", max_length=255)


class course(models.Model):
    """课程表"""
    cnb = models.CharField(verbose_name="课程号", max_length=255)
    cname = models.CharField(verbose_name="课程名", max_length=255)
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE,db_column='Teacher.Ttunmb')#教师id
    #department = models.ForeignKey('Department', on_delete=models.CASCADE)
    cpicture = models.CharField(verbose_name="课程照片", max_length=255)
    create_time = models.DateTimeField(verbose_name="申请通过时间")
    ckind = models.CharField(verbose_name="课程种类", max_length=255)
    credit = models.IntegerField(verbose_name="学分")
    open_time = models.DateTimeField(verbose_name="开课时间")
    cinfo = models.CharField(verbose_name="课程简介", max_length=1000)
    apply_choices = (
                 (0,"未通过"),
                 (1,"通过")
             )
    apply = models.IntegerField(verbose_name="是否申请通过",choices=apply_choices)

class course_selection(models.Model):
    """选课表"""
    course = models.ForeignKey('course', on_delete=models.CASCADE)  # 课程id
    student = models.ForeignKey('Student', on_delete=models.CASCADE)#学生id
    select_time = models.DateTimeField(verbose_name="选课时间")
    grade = models.IntegerField(verbose_name="成绩")