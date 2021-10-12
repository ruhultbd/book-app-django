from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from books.models import books
from books.models import Review

def index(request):

    bookData = books.objects.all()
    data = {
            'title': 'Book Shop',
            'page_titie': 'This is a bookshop',
            'books' : bookData
        }
    return render(request, 'books/index.html', data)

def show(request, id):
    singleBook = get_object_or_404(books, pk=id)
    reviews = Review.objects.filter(book_id=id).order_by('-id')
    data = {
        'title': 'View | Book Shop',
        'page_titie': 'Book Detail Page',
        'book' : singleBook,
        'reviews' : reviews
    }
    return render(request, 'books/show.html', data)

def review(request):
    
    comment = request.POST['comment']
    book_id = request.POST['book_id']
    newComment = Review(comment=comment, book_id=book_id)
    newComment.save()
    messages.add_message(request, messages.SUCCESS, 'Successfully submitted')

    return redirect('/books/'+book_id)
