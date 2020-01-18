from django.db import models
from datetime import datetime

class Author(models.Model):
    name = models.CharField(max_length=32)
    login = models.CharField(max_length=48)
    password = models.CharField(max_length=32)

    def __str__(self):
        return self.name

class Post(models.Model):
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=32)
    text = models.CharField(max_length=256)
    data = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.text