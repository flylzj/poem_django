# coding: utf-8
from .views import PoemIndexView, PoemView
from django.urls import path


app_name = 'poem'

urlpatterns = [
    path('', PoemIndexView.as_view(), name='poem_index'),
    path('<int:pk>/', PoemView.as_view(), name='poem')
]