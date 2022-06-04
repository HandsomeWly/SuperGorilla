# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

from studentApp.models import Student


class Teacher(models.Model):
    """教师表"""
    #Taccount = models.CharField(verbose_name="教师账号",max_length=255)
    password = models.CharField(verbose_name="密码", max_length=255)
    Ttunmb = models.CharField(verbose_name="教师号", max_length=255)
    phonenb = models.CharField(verbose_name="手机号", max_length=11)
    Tname = models.CharField(verbose_name="教师姓名", max_length=255)
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
    course = models.ForeignKey(course, on_delete=models.CASCADE)  # 课程id
    student = models.ForeignKey(Student, on_delete=models.CASCADE)#学生id
    select_time = models.DateTimeField(verbose_name="选课时间")
    grade = models.IntegerField(verbose_name="成绩")


class Task(models.Model):
    """任务表"""
    course = models.ForeignKey('course', on_delete=models.CASCADE)  # 课程id
    Stunmb = models.ForeignKey('Student', on_delete=models.CASCADE)  # 学生id
    putin = models.CharField(verbose_name="任务输入", max_length=1000)
    putinurl = models.CharField(verbose_name="任务路径", max_length=1000)
    finish = models.CharField(verbose_name="任务完成输入", max_length=1000)
    finishurl = models.CharField(verbose_name="任务完成路径", max_length=1000)
    evaluate_choices = (
        (0, "未评价"),
        (1, "已评价")
    )
    evaluate = models.IntegerField(verbose_name="是否评价过", choices=evaluate_choices)
    score_choices = (
        (5,"A"),
        (4, "B"),
        (3, "C"),
        (2, "D"),
        (1, "E")
    )
    score = models.IntegerField(verbose_name="评分", choices=score_choices)

class resource(models.Model):
    """资料表"""
    course = models.ForeignKey('course', on_delete=models.CASCADE)  # 课程id
    resourceurl = models.CharField(verbose_name="资料路径", max_length=1000)