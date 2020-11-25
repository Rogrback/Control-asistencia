from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Assistance
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    TemplateView
)

#List Assistance
class ListAllAssistances(ListView):
    template_name = 'assistance/list_all.html'
    paginate_by = 4
    context_object_name = 'assistance'

    def get_queryset(self):
        key_word = self.request.GET.get("kword_assistance", '')
        lista = Assistance.objects.filter(
            date__icontains=key_word
        )
        return lista
        
#Detail Assistance
class AssistanceDetailView(DetailView):
    template_name = "assistance/detail_assistance.html"
    model = Assistance
    
    def get_context_data(self, **kwargs):
        context = super(AssistanceDetailView, self).get_context_data(**kwargs)
        # All process
        context['titulo'] = 'Asistencia del año'
        return context

#Create assistance
class AssistanceCreateView(CreateView):
    template_name = "assistance/add.html"
    model = Assistance
    fields = ('__all__')
    success_url = '.'

#Update asistance
class AssistanceUpdateView(UpdateView):
    template_name = "assistance/update_state.html"
    model = Assistance
    fields = ('__all__')
    success_url = reverse_lazy('assistance_app:assistance_all')
#Templates
class MainView(TemplateView):
    template_name = "main.html"

