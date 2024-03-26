from django.http import HttpResponse
from django.template import loader


def login(request):
    template = loader.get_template("login.html")
    return HttpResponse(template.render())


def signup(request):
    template = loader.get_template("signup.html")
    return HttpResponse(template.render())


def home(request):
    template = loader.get_template("home.html")
    return HttpResponse(template.render())
