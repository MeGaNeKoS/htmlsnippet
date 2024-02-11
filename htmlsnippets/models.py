from django.db import models


class HTMLSnippet(models.Model):
    title = models.CharField(max_length=100)
    code = models.TextField()
    tag = models.CharField(max_length=50, blank=True, default='General')

