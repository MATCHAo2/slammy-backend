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


class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = ['id', 'name', 'url', 'author']


class WordDetailedSerializer(serializers.ModelSerializer):
    related_words = serializers.SerializerMethodField()
    source = serializers.SerializerMethodField()

    class Meta:
        model = Word
        fields = ['word', 'detailed_description', 'image_url', 'source', 'related_words']

    def get_related_words(self, obj):
        try:
            related_words = Related_Words.objects.filter(word=obj.pk)
            serializer = RelatedWordsSerializer(related_words, many=True)
            output = []
            for r_word in serializer.data:
                tmp_dict = {}
                tmp_dict[Word.objects.values_list('word', flat=True).get(pk=r_word['related'])] = r_word['related']
                output.append(tmp_dict)
            return output
        except:
            return []

    def get_source(self, obj):
            source = Source.objects.filter(name=obj.source)
            serializer = SourceSerializer(source, many=True)
            output = []
            for s_word in serializer.data:
                tmp_dict = {}
                print(s_word)
                tmp_dict[Source.objects.values_list('name', flat=True).get(pk=s_word['id'])] = s_word['id']
                output.append(tmp_dict)
            return output


class RelatedWordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Word
        fields = ['related']
