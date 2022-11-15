from django.http import HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views import generic
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import WordSerializer, WordDetailedSerializer, SourceSerializer, RelatedWordSerializer
from .models import Word, Source, Related_Words


def Index(request):
    return HttpResponse("Index page")


class WordViewSet(viewsets.ModelViewSet):
    # API endpoint that allows Words to be viewed or created.
    queryset = Word.objects.all()
    serializer_class = WordSerializer
    permission_classes = [permissions.IsAuthenticated]


class SourceViewSet(viewsets.ModelViewSet):
    # API endpoint that allows Source to be viewed or created.
    queryset = Source.objects.all()
    serializer_class = SourceSerializer
    permission_classes = [permissions.IsAuthenticated]


class RelatedWordViewSet(viewsets.ModelViewSet):
    # API endpoint that allows Related_Words to be viewed or created.
    queryset = Word.objects.all().prefetch_related("related_words").values("related_words__related").all()
    serializer_class = RelatedWordSerializer
    permission_classes = [permissions.IsAuthenticated]
