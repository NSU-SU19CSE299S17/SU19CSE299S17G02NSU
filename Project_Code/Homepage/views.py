from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
  return render(request, 'Homepage/index.html')
  return HttpResponse (template.render(context,request))

def books(request):
  return render(request, 'Homepage/books.html')


