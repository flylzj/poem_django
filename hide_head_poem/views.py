from django.shortcuts import render
from django.views import generic
from utils.TangshiGene2 import Line5_Head


class HideHeadIndexView(generic.View):
    def get(self, request):
        return render(
            request,
            'head/head.html'
        )


class HideHeadView(generic.View):
    def get(self, request, **kwargs):

        head = kwargs.get("head")
        try:
            res = Line5_Head(head)
            res = res.split("\n")
        except Exception as e:
            res = [
                "抱歉!",
                "{}无法生成藏头诗".format(head),
            ]
        return render(
            request,
            'head/head.html',
            {
                "lines": res
            }
        )

