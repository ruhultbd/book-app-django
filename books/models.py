from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, TextField
from django.contrib.auth.models import User

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"{self.name}"

class Book(models.Model):
    title = models.CharField(max_length=200)
    isbn = models.CharField(max_length=150, null=True)
    pageCount = models.IntegerField(default=0)
    longDescription = models.TextField(null=True)
    #publishedDate = models.DateTimeField(null=True)    
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
    authors = models.ManyToManyField(Author)
    image = models.ImageField(upload_to='books_thumbs', null=True)

    def __str__(self):
        return f"{self.title}"

class Review(models.Model):
    comment = models.TextField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now=True, null=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='preview', null=True)

    

