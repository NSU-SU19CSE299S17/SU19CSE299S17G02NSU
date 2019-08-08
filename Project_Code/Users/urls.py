from django.urls import path
from . import views
from .views import viewBooks
from .models import MyLibraryList


urlpatterns = [
#   path('', views.users, name ='users')
path('viewBooks/', viewBooks, views.ListView.as_view(model=MyLibraryList))
#path('viewBooks/', views.ListView.as_view(model=MyLibraryList))
]
