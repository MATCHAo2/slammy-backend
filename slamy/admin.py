from django.contrib import admin
from .models import Word, Source
from import_export.resources import ModelResource
from import_export.admin import ImportExportMixin
from import_export.formats import base_formats
from .models import Word, Related_Words


class WordResource(ModelResource):
    class Meta:
        model = Word

        import_order = ('id', 'word', 'short_description', 'detailed_description', 'image_url', 'source')
        import_id_fields = ['id']

class WordAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('id', 'word', 'short_description', 'detailed_description', 'image_url', 'source')
    resource_class = WordResource
    formats = [base_formats.CSV]

admin.site.register(Word, WordAdmin)
admin.site.register(Source)
admin.site.register(Related_Words)
