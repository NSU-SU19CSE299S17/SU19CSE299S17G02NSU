from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def browser(request):
    return HttpResponse("<h1> Welcome to browsing page </h1>")