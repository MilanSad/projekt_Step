from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from random import choice


"""def home_page(request):

    return HttpResponse("Hello world!")"""

def home_page(request):
    template = loader.get_template("home.html")
    return HttpResponse(template.render())

def news(request):
    template = loader.get_template("news.html")
    return HttpResponse(template.render())

def management(request):
    template = loader.get_template("management.html")
    return HttpResponse(template.render())

def about_company(request):
    template = loader.get_template("about_company.html")
    return HttpResponse(template.render())

def news2(request):
    template = loader.get_template("news2.html")
    sentence = choice(["veta1", "veta2", "veta3", "veta3"])
    context = {
        "sentence": sentence,
    }
    return HttpResponse(template.render(context, request))