from django.contrib import admin

# # Register your models here.
# from .models import Books
# from import_export.admin import ImportExportModelAdmin


# class ViewAdmin(ImportExportModelAdmin):
#     resource_class = Books


# admin.site.register(Books, ViewAdmin)
# # # admin.site.register(Books)

from import_export import resources
from .models import Books

class BookResource(resources.ModelResource):

    class Meta:
        model = Books
        skip_unchanged = True
        report_skipped = True
        exclude = ('id',)
        import_id_fields = ("Book_ID", "Title", "Author", "Genre1", "Genre2", "Plot")



from import_export.admin import ImportExportModelAdmin


class BookAdmin(ImportExportModelAdmin):
    resource_class = BookResource

admin.site.register(Books, BookAdmin)