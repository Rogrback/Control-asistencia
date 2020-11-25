from django.shortcuts import render
from .models import Teacher
from django.views.generic import (
    ListView,
    DetailView,
    CreateView
)
from django.views.generic.edit import FormView
from .forms import NewTeacherForm
from applications.user_type.models import UserType

class ListAllTeachers(ListView):
    template_name = 'teacher/list_all.html'
    model = Teacher

class TeacherDetailView(DetailView):
    template_name = "teacher/detail_teacher.html"
    model = Teacher

class TeacherCreateView(CreateView):
    template_name = "teacher/add.html"
    model = Teacher
    fields = ('__all__')
    success_url = '.'
    
class NewTeacherView(FormView):
    template_name = 'teacher/new_teacher.html'
    form_class = NewTeacherForm
    success_url = '/'

    def form_valid(self, form):
        print('*******Estamos en el form valid*******')
        id_card = form.cleaned_data['id_card']
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        phone = form.cleaned_data['phone']
        user = form.cleaned_data['user']
        password = form.cleaned_data['password']
        UserType.objects.create(
            name=name
        )        
        return super(NewTeacherView, self).form_valid(form)