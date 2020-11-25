from django.contrib import admin
from django.urls import path
from . import views

app_name = "assistance_app"

urlpatterns = [
    path(
        '',
        views.MainView.as_view(),
        name='main'
    ),
    path(
        'listar-asistencias/',
        views.ListAllAssistances.as_view(),
        name='assistance_all'
    ),
    path(
        'ver-asistencia/<pk>/',
        views.AssistanceDetailView.as_view()
    ),
    path(
        'agregar-asistencia/',
        views.AssistanceCreateView.as_view(),
        name='create_assistance'
    ),
    path(
        'editar-asistencia/<pk>/',
        views.AssistanceUpdateView.as_view(),
        name='update_assistance'
    )
]