from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def Recommender(request):
  return render(request, 'Recommender/Recommender.html')
  return HttpResponse (template.render(context,request))

