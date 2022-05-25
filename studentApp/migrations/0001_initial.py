# Generated by Django 3.2.13 on 2022-05-24 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=255, verbose_name='密码')),
                ('Stunmb', models.CharField(max_length=255, verbose_name='学号')),
                ('phonenb', models.CharField(max_length=11, verbose_name='手机号')),
                ('Sname', models.CharField(max_length=255, verbose_name='学生姓名')),
                ('School', models.CharField(max_length=255, verbose_name='学校')),
            ],
        ),
    ]