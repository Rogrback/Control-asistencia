from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('listar-tipos-usuario/', views.ListAllUserType.as_view()),
    path('ver-tipo-usuario/<pk>/', views.UserTypeDetailView.as_view()),
    path('agregar-tipo-usuario/', views.UserTypeCreateView.as_view()),
]