from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


"""def home_page(request):

    return HttpResponse("Hello world!")"""

def home_page(request):
    template = loader.get_template("home.html")
    return HttpResponse(template.render())

def news(request):
    template = loader.get_template("news.html")
    return HttpResponse(template.render())