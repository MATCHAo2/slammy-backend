from .models import Word, Source, Related_Words
from rest_framework import serializers

class WordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Word
        fields = ['id', 'word', 'short_description']


class RelatedWordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Related_Words
        fields = ['related', 'id']


class WordDetailedSerializer(serializers.ModelSerializer):
    related_words = serializers.SerializerMethodField()

    class Meta:
        model = Word
        fields = ['word', 'detailed_description', 'image_url', 'source', 'related_words']

    def get_related_words(self, obj):
        try:
            related_words = Related_Words.objects.filter(word=obj.pk)
            print(related_words)
            serializer = RelatedWordsSerializer(related_words, many=True)
            output = []
            for r_word in serializer.data:
                tmp_dict = {}
                tmp_dict[Word.objects.values_list('word', flat=True).get(pk=r_word['related'])] = r_word['related']
                output.append(tmp_dict)
            return output
        except:
            return []


class SourceSerializer(serializers.HyperlinkedModelSerializer): 
    class Meta:
        model = Source
        fields = ['name', 'url', 'author']


class RelatedWordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Word
        fields = ['related']
