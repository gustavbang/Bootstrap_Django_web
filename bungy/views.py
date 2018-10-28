import datetime

#for forms.py
from bungy.forms import LoginForm

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

def test(request):
    today = datetime.datetime.now().date()
    daysOfWeek = ["mon", "tue", "wed", "thur", "fri", "sat", "sun"]
    return render(request, "test.html", {"today" : today, "days_of_week": daysOfWeek})


def login(request):
    return render(request, "login.html", {})


def loggedin(request):
    username = "not logged in"
    if request.method == "POST":
        MyLoginForm = LoginForm(request.POST)
        if MyLoginForm.is_valid():
            print("hej")
            username = MyLoginForm.cleaned_data['username']
        else:
            MyLoginForm = LoginForm()

    return render(request, "loggedin.html", {"username": username})