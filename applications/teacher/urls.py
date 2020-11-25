from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('listar-docentes/', views.ListAllTeachers.as_view()),
    path('ver-docente/<pk>/', views.TeacherDetailView.as_view()),
    path('agregar-docente/', views.TeacherCreateView.as_view()),
    path('new-teacher/', views.NewTeacherView.as_view(), name='nuevo_profesor'),
]