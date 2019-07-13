from django.shortcuts import render
from django.http import HttpResponse
from .models import Books
from django.db.models import Q
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.

def browser(request):
  if request.method=='POST':
      srch = request.POST['srh']

      if srch:
        match = Books.objects.filter(Q(Title__icontains=srch) | Q(Author__icontains=srch)  )

        if match:
             return render(request, '/Browser/', {'sr':match})
        else:
             messages.error(request,'no results found')

      else:
         return HttpResponseRedirect('/Browser/')

  else:
    return render(request, 'Browser/browser.html')