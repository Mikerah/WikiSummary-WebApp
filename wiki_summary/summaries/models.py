from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    full_article = models.CharField(max_length=250)
    