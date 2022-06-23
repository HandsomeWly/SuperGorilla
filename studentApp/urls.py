from django.urls import path, include
from studentApp import views
from studentApp import mydatabase
urlpatterns = [
    path('index/', views.index),
    path('studentRegister/', views.studentRegister),
    path('studentLogin/', views.studentLogin),
    path('courseInformation/', views.courseInformation),
    path('DBcourseInformation/', mydatabase.courseInformation),
    path('DBselfCourseInformation/<username>',mydatabase.self_class_Info),
    path('courseSelect/', views.courseSelect),
    path('deleteCourse/',views.deleteCourseInfo),
    path('studentLoginAxois/', views.studentLoginUseAxois_Tmp),
    path('studentRegisterAxois', views.studentRegisterUseAxois_Tmp),
    path('example_Picture/',views.example_Picture),
    path('picture/',views.example_Picture),
    path('picture/<name>',views.picture),
    path('document/',views.example_Document),
    path('upload/<cname>',views.getTheDocument),
    path('getFiles/<cname>',mydatabase.fileList),
    path('downloadfile/<cname>&<filename>',views.downloadfile),
    path('deleteFile/',mydatabase.delete_file),
    path('studentInfo/<username>',mydatabase.studen_Info),
    path('uploadPicture/<stunum>',views.upload_picture),
    path('changeInfo/',mydatabase.change_student_Info)
]