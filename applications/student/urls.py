from django.contrib import admin
from django.urls import path
from . import views

app_name = "student_app"

urlpatterns = [
    path(
        'listar-estudiantes/', 
        views.ListAllStudents.as_view()
        ),
    #path('listar-estudiante-por-genero/', views.ListByGender.as_view()),
    path('buscar-estudiante/', views.ListStudentsByKword.as_view()),
    path('buscar-estudiante-por-curso/', 
        views.ListStudentByCourse.as_view(), 
        name='student_course'
        ),
    path(
        'ver-estudiante/<pk>/',
        views.StudentDetailView.as_view(),
        name='student_profile'
        ),
    path('agregar-estudiante/', views.StudentCreateView.as_view()),    
    path('actualizar-estudiante/<pk>/', views.StudentUpdateView.as_view()),
    path('eliminar-estudiante/<pk>/', views.StudentDeleteView.as_view()),
    path('creado/', views.SuccessfullyCreatedView.as_view(), name='successfully-created'),
    path('actualizado/', views.SuccessfullyUpdatedView.as_view(), name='successfully-updated'),
    path('eliminado/', views.SuccessfullyDeletedView.as_view(), name='successfully-deleted'),
]