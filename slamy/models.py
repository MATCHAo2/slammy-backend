from django.db import models


class Source(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    url = models.URLField(null=True, blank=True)
    author = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name


class Word(models.Model):
    word = models.CharField(max_length=50, null=False, blank=False)
    short_description = models.CharField(max_length=100, null=False, blank=False)
    detailed_description = models.TextField(max_length=500, null=True, blank=False)
    image_url = models.ImageField(upload_to='images/', null=True, blank=True)
    source = models.ForeignKey(Source, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.word


class Related_Words(models.Model):
    word = models.ForeignKey(Word, on_delete=models.CASCADE, null=False, blank=False, related_name='related_words')
    related = models.ForeignKey(Word, on_delete=models.CASCADE, null=False, blank=False, related_name='+')
