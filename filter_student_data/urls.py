from django.contrib import admin
from django.urls import path

from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('data/<lst>',views.data,name='data')
]
