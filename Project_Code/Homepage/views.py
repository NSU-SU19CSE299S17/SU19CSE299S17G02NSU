from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
  # return HttpResponse("<h1> Welcome to Bookworm </h1>")
   template = loader.get_template(Homepage/index.html)
   return render(request, 'Homepage/index.html')
  # return HttpResponse (template.render(context,request))
