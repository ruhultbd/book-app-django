from django.contrib import admin
from django.db import models
from books.models import books


# Register your models here.

admin.site.register(books)