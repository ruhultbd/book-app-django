from django.db import models
from django.db.models.fields import CharField, TextField

# Create your models here.

class books(models.Model):
    title = models.CharField(max_length=200)
    isbn = models.CharField(max_length=150, null=True)
    thumnail = models.CharField(max_length=300, null=True)
    pageCount = models.IntegerField(default=0)
    longDescription = models.TextField(null=True)
    #publishedDate = models.DateTimeField(null=True)
    authors = models.TextField(null=True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)


class Review(models.Model):
    book_id = models.IntegerField()
    comment = models.TextField(null=True)
    user_id = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now=True, null=True)
    updated_at = models.DateTimeField(null=True)

