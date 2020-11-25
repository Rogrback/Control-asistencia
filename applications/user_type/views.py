from django.shortcuts import render
from .models import UserType
from django.views.generic import (
    ListView,
    DetailView,
    CreateView
)

class ListAllUserType(ListView):
    template_name = 'user_type/list_all.html'
    model = UserType

class UserTypeDetailView(DetailView):
    template_name = "user_type/detail_user_type.html"
    model = UserType
    
    def get_context_data(self, **kwargs):
        context = super(UserTypeDetailView, self).get_context_data(**kwargs)
        # All proccess
        context['titulo'] = 'Tipo de Usuario'
        return context

class UserTypeCreateView(CreateView):
    template_name = "user_type/add.html"
    model = UserType
    fields = ('__all__')
    success_url = '.'