from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', home_page, name="home_page"),
    path('news', news, name="news"),
]