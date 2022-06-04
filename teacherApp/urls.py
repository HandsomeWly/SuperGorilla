from django.urls import path, include
from teacherApp import views

urlpatterns = [
    path('index/', views.index),
    path('courseApplication/',views.teacher_course_application),
    path('setHomework/',views.set_homework)
]