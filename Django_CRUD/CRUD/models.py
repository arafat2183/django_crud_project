from django.db import models

class BookList(models.Model):
    title = models.CharField(max_length=150)
    price = models.IntegerField()
    author = models.CharField(max_length=100)
