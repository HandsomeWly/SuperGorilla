from django.urls import path, include
from adminApp import views

urlpatterns = [
    path('index/', views.index),
    path('courseInformation/',views.courseInformation),
    path('studentInformation/',views.studentInformation),
    path('teacherInformation/',views.teacherInformation)

]