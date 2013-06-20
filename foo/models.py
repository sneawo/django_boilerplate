from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('article-detail', [self.pk])
