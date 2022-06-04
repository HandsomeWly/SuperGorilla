from django.urls import path, include
from studentApp import views

urlpatterns = [
    path('index/', views.index),
    path('studentRegister/', views.studentRegister),
    path('studentLogin/', views.studentLogin),
    path('courseInformation/', views.courseInformation),
    path('courseSelect/', views.courseSelect),
    path('studentLoginAxois/', views.studentLoginUseAxois_Tmp),
    path('studentRegisterAxois', views.studentRegisterUseAxois_Tmp),
    path('example_Picture/',views.example_Picture),
    path('picture/',views.example_Picture),
    path('picture/<name>',views.picture),
    path('document/',views.example_Document),
    path('upload/',views.getTheDocument)
]