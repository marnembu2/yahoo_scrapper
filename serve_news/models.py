from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.TextField(max_length=1000)
    description = models.TextField(null=True, blank=True)
    guid = models.TextField(null=True, max_length=500)
    guid_is_perma_link = models.BooleanField(default=False)
    link = models.TextField(max_length=1000)
    pubDate = models.DateTimeField()

    def __str__(self):
        return self.title + self.description
