from django.shortcuts import render
from django.views import generic
from poet_recommendation.models import Poet
from poem_recommendation.models import Poem


class SearchView(generic.View):
    def get(self, request, **kwargs):
        text = kwargs.get('text')
        if not text:
            return
        poem_list = Poem.objects.filter(content__contains=text)
        poet_list = Poet.objects.filter(name__contains=text)
        context = {
            "poem_list": poem_list,
            "poet_list": poet_list
        }
        return render(
            request,
            'search/search.html',
            context
        )

