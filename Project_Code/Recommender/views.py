from django.shortcuts import render
from django.http import HttpResponse
from .recommend import customs
from .recommend import recommend


# Create your views here.

def Recommender(request):
  return render(request, 'Recommender/Recommender.html')
  return HttpResponse (template.render(context,request))


def output(request):
  return render(request, 'Recommender.html', {'output': recommend(customs('Playing with Fire'))})

