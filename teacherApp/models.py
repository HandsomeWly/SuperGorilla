from django.db import models


# Create your models here.
class Teacher(models.Model):
    """教师表"""
    #Taccount = models.CharField(verbose_name="教师账号",max_length=255)
    password = models.CharField(verbose_name="密码", max_length=255)
    Ttunmb = models.CharField(verbose_name="教师号", max_length=255)
    phonenb = models.CharField(verbose_name="手机号", max_length=11)
    Tname = models.CharField(verbose_name="教师姓名", max_length=255)
    School = models.CharField(verbose_name="学校", max_length=255)


'''class Task(models.Model):
    """任务表"""
    course = models.ForeignKey(course, on_delete=models.CASCADE)  # 课程id
    Stunmb = models.ForeignKey(Student, on_delete=models.CASCADE)  # 学生id
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
    '''