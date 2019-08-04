from django.contrib import admin
from .models import MyLibraryList
from .models import Profile
from .models import UserList

admin.site.register(Profile)
admin.site.register(MyLibraryList)
admin.site.register(UserList)

