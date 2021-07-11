from django.contrib import admin
from .models import Comments
from import_export.admin import ImportExportModelAdmin


class InlineComments(admin.TabularInline):
    model = Comments


class CommentsAdmin(ImportExportModelAdmin):
    list_filter = ('author', 'create_date')
    list_display = ('id', 'author', 'create_date', 'text')
    list_display_links = ('id', 'author', 'create_date', 'text')
    search_fields = ('author', 'create_date', 'text')
# Register your models here.


admin.site.register(Comments, CommentsAdmin)
