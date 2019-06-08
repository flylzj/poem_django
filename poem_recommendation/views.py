from django.shortcuts import render
from django.views import generic
from .models import Poem
import random

# Create your views here.


class PoemIndexView(generic.ListView):
    template_name = 'poem_recommendation/poem.html'
    context_object_name = 'poem_list'
    poems = [
        {
            "title": "江南",
            "content": "江南可采莲，莲叶何田田，鱼戏莲叶间。鱼戏莲叶东，鱼戏莲叶西，鱼戏莲叶南，鱼戏莲叶北。",
            "href": "../../../static/江南.html"
        },
        {
            "title": "咏鹅",
            "content": "鹅鹅鹅，曲项向天歌。白毛浮绿水，红掌拨清波。",
            "href": "../../../static/咏鹅.html"
        },
        {
            "title": "枫桥夜泊",
            "content": "月落乌啼霜满天，江枫渔火对愁眠。姑苏城外寒山寺，夜半钟声到客船",
            "href": "../../../static/枫桥夜泊.html"
        },
        {
            "title": "静夜思",
            "content": "床前明月光，疑是地上霜。举头望明月，低头思故乡。",
            "href": "../../../static/静夜思.html"
        }
    ]

    def get_queryset(self):
        count = Poem.objects.all().count()
        rand = random.sample(range(count), 10)
        return Poem.objects.filter(id__in=rand)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['r_poem'] = random.choice(self.poems)
        return context


class PoemView(generic.DetailView):
    template_name = 'poem_recommendation/poem.html'
    context_object_name = 'poem'
    model = Poem