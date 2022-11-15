from .models import Word, Source, Related_Words
from rest_framework import serializers

class WordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Word
        fields = ['id', 'word', 'short_description']


class RelatedWordsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Related_Words
        fields = ['related', 'id']


class WordDetailedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Word
        fields = ['word', 'detailed_description', 'image_url', 'source', 'related_words']

    def get_related_words(self, obj):
        try:
            related_words = Words.objects.prefetch_related("related_words").values("related_words__related").all()
            serializer = RelatedWordsSerializer(related_words, many=True)
            output = []
            for r_word in serializer.data:
                tmp_dict = {}
                tmp_dict[r_word["related"]] = self.context['request']._current_scheme_host + r_word["id"]
                output.append(tmp_dict)
            return output
        except:
            return ""


class SourceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Source
        fields = ['name', 'url', 'author']


class RelatedWordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Word
        fields = ['related']
