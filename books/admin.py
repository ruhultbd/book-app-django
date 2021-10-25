from django.contrib import admin
from django.db import models
from books.models import Author, Book


# Register your models here.

admin.site.register(Book)
admin.site.register(Author)