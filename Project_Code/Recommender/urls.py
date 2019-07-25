from django.urls import path
from . import views

urlpatterns = [
    path('', views.Recommender, name ='Recommender'),

]
