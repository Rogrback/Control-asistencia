from django.contrib import admin
from django.urls import path
from . import views

app_name = "course_app"

urlpatterns = [
    path('listar-cursos/', views.ListAllCourses.as_view()),
    path('ver-curso/<pk>/', views.CourseDetailView.as_view()),
    path('agregar-curso/', views.CourseCreateView.as_view()),
    path('actualizar-curso/<pk>/', views.CourseUpdateView.as_view()),
    path('eliminar-curso/<pk>/', views.CourseDeleteView.as_view()),
    path('creado/', views.SuccessfullyCreatedView.as_view(), name='successfully-created'),
    path('actualizado/', views.SuccessfullyUpdatedView.as_view(), name='successfully-updated'),
    path('eliminado/', views.SuccessfullyDeletedView.as_view(), name='successfully-deleted'),
]