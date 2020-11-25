from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('listar-grados/', views.ListAllGrades.as_view()),
    path('ver-grado/<pk>/', views.GradeDetailView.as_view()),
    path('agregar-grado/', views.GradeCreateView.as_view()),
]