# coding: utf-8
from django.urls import path
from .views import SearchView

app_name = 'search'

urlpatterns = [
    path('<str:text>/', SearchView.as_view(), name='search')
]