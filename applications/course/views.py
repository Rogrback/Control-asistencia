from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Course
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView
)

#List courses
class ListAllCourses(ListView):
    template_name = 'course/list_all.html'
    model = Course

#Detail courses
class CourseDetailView(DetailView):
    template_name = "course/detail_course.html"
    model = Course

    def get_context_data(self, **kwargs):
        context = super(CourseDetailView, self).get_context_data(**kwargs)
        # All proccess
        context['titulo'] = 'Curso del año'
        return context

#Create course
class CourseCreateView(CreateView):
    template_name = "course/add.html"
    model = Course
    fields = ('__all__')
    success_url = reverse_lazy('course_app:successfully-created')

#Update course
class CourseUpdateView(UpdateView):
    template_name = "course/update.html"
    model = Course
    fields = ('__all__')
    success_url = reverse_lazy('course_app:successfully-updated')

#Delete course
class CourseDeleteView(DeleteView):
    model = Course
    template_name = "course/delete.html"
    success_url = reverse_lazy('course_app:successfully-deleted')

#Templates
class SuccessfullyCreatedView(TemplateView):
    template_name = "course/success_created.html"

class SuccessfullyUpdatedView(TemplateView):
    template_name = "course/success_updated.html"

class SuccessfullyDeletedView(TemplateView):
    template_name = "course/success_deleted.html"
