from django.shortcuts import render
from django.http import HttpResponse

import json

bookData = open('/opt/lampp/htdocs/python/mysite/books.json').read()
books = json.loads(bookData)

def index(request):
    data = {
            'title': 'Book Shop',
            'page_titie': 'This is a bookshop',
            'books' : books
        }
    return render(request, 'books/index.html', data)


def show(request, id):
    singleBook = list()
    for book in books:
        if book['id'] == id:
            singleBook = book


    data = {
            'title': 'View | Book Shop',
            'page_titie': 'Book Detail Page',
            'book' : singleBook
        }
    return render(request, 'books/show.html', data)