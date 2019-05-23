from django.shortcuts import render
from django.views import generic
from .models import Poet
import random


class PoetIndexView(generic.ListView):
    template_name = '../templates/main.html'
    context_object_name = 'poet_list'

    def get_queryset(self):
        count = Poet.objects.all().count()
        rand = random.sample(range(count), 10)
        return Poet.objects.filter(id__in=rand)


class PoetView(generic.DetailView):
    template_name = 'poet_recommendation/poet.html'
    model = Poet
    context_object_name = 'poet'

