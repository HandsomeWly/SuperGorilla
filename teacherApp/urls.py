from django.urls import path, include
from teacherApp import views

urlpatterns = [
    path('index/', views.index),
    path('courseApplication/',views.teacher_course_application),
    path('setHomework/',views.set_homework),
    path('teacherLogin/',views.teacherLogin),
    path('changeCourseTime/',views.change_course_Date),
    path('changeCoursePosition/',views.change_course_Position),
    path('deleteCourse/',views.delete_Course)
]