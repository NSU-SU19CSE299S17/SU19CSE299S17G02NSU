from django.shortcuts import render
from django.http import HttpResponse
from .recommend import customs
from .recommend import recommend


# Create your views here.

def Recommender(request):
  if request.method == 'POST':
    srch = request.POST['srh']

    if srch:
      fin = recommend(customs(srch))

      if fin:
        return render(request, 'Recommender/Recommender.html', {'sr': fin})
      else:
        raise Exception('Not Found!!')

    else:
      return render(request, 'Recommender/Recommender.html')


  else:
    return render(request, 'Recommender/Recommender.html')
    return HttpResponse(template.render(context, request))
