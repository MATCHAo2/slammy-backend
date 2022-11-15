from .models import Word, Source
from rest_framework import serializers

class WordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Word
        fields = ['id', 'word', 'short_description']


class WordDetailedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Word
        fields = ['word', 'detailed_description', 'image', 'source']


class SourceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Source
        fields = ['name', 'url', 'author']


class RelatedWordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Word
        fields = ['related']
