from django.contrib import admin
from .models import Word, Source
from import_export import resources
from import_export.admin import ImportExportMixin
from .models import Word, Related_Words

admin.site.register(Word)
admin.site.register(Source)
admin.site.register(Related_Words)


class WordResource(resources.ModelResource):
    class Meta:
        model = Word
        fields = ('word', 'short_description', 'detailed_description')

class WordAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = WordResource
    pass


