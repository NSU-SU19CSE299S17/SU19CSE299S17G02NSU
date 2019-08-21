from django.urls import path
from . import views
from .models import MyLibraryList


urlpatterns = [
    path('', views.Recommender, name='Recommender'),
]
