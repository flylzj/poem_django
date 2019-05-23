from django.shortcuts import render
from django.views import generic

# Create your views here.

class PoemIndexView(generic.ListView):
    template_name = '../templates/index.html'
    context_object_name = 'poem_list'

    def get_queryset(self):
        return None
