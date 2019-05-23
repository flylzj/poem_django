# coding: utf-8
from .views import PoetIndexView, PoetView
from django.urls import path

app_name = 'poet'

urlpatterns = [
    path('', PoetIndexView.as_view(), name='poet_index'),
    path('<int:pk>', PoetView.as_view(), name='poet')
]