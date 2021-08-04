from django.db import models


class Article(models.Model):
    title = models.TextField(max_length=1000)
    description = models.TextField(null=True, blank=True)
    guid = models.TextField(null=True, max_length=500)
    guid_is_perma_link = models.BooleanField(default=False)
    link = models.TextField(max_length=1000)
    pubDate = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.guid + ' | ' + self.title + ' | ' + self.description
