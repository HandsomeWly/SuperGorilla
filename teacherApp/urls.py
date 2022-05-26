from django.urls import path, include
from teacherApp import views

urlpatterns = [
    path('index/', views.index)
]