from django.shortcuts import render
from django.views import generic
from .models import Poem
import random

# Create your views here.


class PoemIndexView(generic.ListView):
    template_name = '../templates/main.html'
    context_object_name = 'poem_list'

    def get_queryset(self):
        count = Poem.objects.all().count()
        rand = random.sample(range(count), 10)
        return Poem.objects.filter(id__in=rand)


class PoemView(generic.DetailView):
    template_name = 'poem_recommendation/poem.html'
    context_object_name = 'poem'
    model = Poem