from django.urls import path
from . import views
from .views import viewBooks


urlpatterns = [
#   path('', views.users, name ='users')
path('viewBooks/', viewBooks)

]
