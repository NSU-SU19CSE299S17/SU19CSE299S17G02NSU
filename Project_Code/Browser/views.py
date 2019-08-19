from django.shortcuts import render
from django.http import HttpResponse
from .models import Books
from django.db.models import Q
from django.contrib import messages
from django.http import HttpResponseRedirect
from ..Users.models import MyLibraryList


# Create your views here.

def browser(request):
  if request.method=='POST':
      srch = request.POST['srh']

      if srch:
        match = Books.objects.filter(Q(Title__icontains=srch) | Q(Author__icontains=srch)  )

        if match:
             return render(request, 'Browser/browser.html', {'sr':match})
        else:
            raise Exception('Not Found!!')
            #displays django's error page instead of showing error message in browser page
            #messages.error(request,'No Results Found!')


      else:
          return render(request, 'Browser/browser.html')
          #return HttpResponseRedirect('/Browser/browser.html')

  else:
    return render(request, 'Browser/browser.html')



def AddBooks(request):
    if request.GET.get('add-btn'):
        current_user = request.user
        if request.user.is_authenticated:
            f1 = MyLibraryList.objects.create(UserID=current_user, name=Name, author=Author, genre=Genre)
            context = {
                'c' : f1
            }
            return render(request, 'Users/mylibrary.html', context)
        else:
            raise Exception('User doesnt exist')
            return render(request, 'Users/mylibrary.html')

