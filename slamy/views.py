from django.http import HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views import generic
from .models import Word, Source

def Index(request):
    return HttpResponse("Index page")
