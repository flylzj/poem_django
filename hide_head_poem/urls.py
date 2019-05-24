# coding: utf-8
from django.urls import path
from .views import HideHeadView, HideHeadIndexView


app_name = 'hide_head'

urlpatterns = [
    path('', HideHeadIndexView.as_view(), name="head_index"),
    path('<str:head>/', HideHeadView.as_view(), name='head')
]