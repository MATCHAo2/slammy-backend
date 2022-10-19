import csv
import io
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views import generic
from .models import Word, Source

def Index(request):
    return HttpResponse("Index page")


class CSVImport(generic.FormView):
    template_name = 'app/import.html'
    success_url = reverse_lazy('app:index')
    form_class = CSVUploadForm

    def form_valid(self, form):
        csvfile = io.TextIOWrapper(form.cleaned_data['file'], encoding='utf-8')
        reader = csv.reader(csvfile)
        for row in render:
            word, created = Word.objects.get_or_create(pk=row[0])
            word.word = row[1]
            word.save()
        return super().form_valid(form)

