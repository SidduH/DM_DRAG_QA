from django.db import models


# Create your models here.
class Document():
    title = models.CharField('title', max_length=255)
    content = models.TextField(
        'Content', blank=True, null=True, max_length=2000)
