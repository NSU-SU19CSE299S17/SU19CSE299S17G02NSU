from django.contrib import admin
from .models import BookList
from .models import Profile

admin.site.register(Profile)
admin.site.register(BookList)
