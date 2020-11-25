from django.shortcuts import render
from .models import Grade
from django.views.generic import (
    ListView,
    DetailView,
    CreateView
)

class ListAllGrades(ListView):
    template_name = 'grade/list_all.html'
    model = Grade

class GradeDetailView(DetailView):
    template_name = "grade/detail_course.html"
    model = Grade

    def get_context_data(self, **kwargs):
        context = super(GradeDetailView, self).get_context_data(**kwargs)
        # All proccess
        context['titulo'] = 'Curso del año'
        return context

class GradeCreateView(CreateView):
    template_name = "grade/add.html"
    model = Grade
    fields = ('__all__')
    success_url = '.'


    