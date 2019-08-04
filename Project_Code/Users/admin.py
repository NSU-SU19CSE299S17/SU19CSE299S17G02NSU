from django.contrib import admin
from .models import MyLibraryList
from .models import Profile

admin.site.register(Profile)
admin.site.register(MyLibraryList)
