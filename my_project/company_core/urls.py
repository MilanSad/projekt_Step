from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', home_page, name="home_page"),
    path('news', news, name="news"),
    path('management', management, name="management"),
    path('about_company', about_company, name="about_company"),
    path('news2', news2, name="news2"),
]