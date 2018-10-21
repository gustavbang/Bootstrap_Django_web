from django.shortcuts import render

# Create your views here.

from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render, redirect


def index(request):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def info(request):
    template = loader.get_template('info.html')
    context = {}
    return HttpResponse(template.render(context, request))

def overview(request):
    template = loader.get_template("overview.html")
    context = {}
    return HttpResponse(template.render(context, request))