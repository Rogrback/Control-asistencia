from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Student
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView
)

#List students
class ListAllStudents(ListView):
    template_name = 'student/list_all.html'
    paginate_by = 3
    model = Student

#List students by kword
class ListStudentsByKword(ListView):
    template_name = 'student/by_kword.html'    
    context_object_name = 'student'

    def get_queryset(self):
        key_word = self.request.GET.get("kword", '')
        students_list = Student.objects.filter(
            first_name=key_word
        )
        return students_list

class ListStudentByCourse(ListView):
    template_name = 'student/by_course.html'
    paginate_by = 3
    ordering = "last_name"
    context_object_name = 'student'
    queryset = Student.objects.filter(
        grade__name='INICIAL'
    ).order_by("student_enrollment")

    def get_queryset(self):
        key_word = self.request.GET.get("kword_student", '')
        lista = Student.objects.filter(
            last_name__icontains=key_word
        )
        return lista

#Detail student
class StudentDetailView(DetailView):
    template_name = "student/detail_student.html"
    model = Student
    
    def get_context_data(self, **kwargs):
        context = super(StudentDetailView, self).get_context_data(**kwargs)
        # All process
        context['titulo'] = 'Estudiante del año'
        return context

#Create student
class StudentCreateView(CreateView):
    template_name = "student/add.html"
    model = Student
    fields = ('__all__')
    success_url = reverse_lazy('student_app:successfully-created')

#Update student
class StudentUpdateView(UpdateView):
    template_name = "student/update.html"
    model = Student
    fields = ('__all__')
    success_url = reverse_lazy('student_app:successfully-updated')
    """
    def post(self, request, *args, **kwargs):
        self.objects = self.get_object()
        print(request.POST)
        print(request.POST['last_name'])
        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form):
        return super(StudentUpdateView, self).form_valid(form)
    """

#Delete student
class StudentDeleteView(DeleteView):
    model = Student
    template_name = "student/delete.html"
    success_url = reverse_lazy('student_app:successfully-deleted')

#Templates
class SuccessfullyCreatedView(TemplateView):
    template_name = "student/success_created.html"

class SuccessfullyUpdatedView(TemplateView):
    template_name = "student/success_updated.html"

class SuccessfullyDeletedView(TemplateView):
    template_name = "student/success_deleted.html"

    
