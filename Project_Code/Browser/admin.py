from django.contrib import admin

# Register your models here.
from .models import Books
from import_export.admin import ImportExportModelAdmin


class ViewAdmin(ImportExportModelAdmin):
    resource_class = Books


admin.site.register(Books, ViewAdmin)