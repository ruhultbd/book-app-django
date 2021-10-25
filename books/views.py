from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
import books
from books.models import Book, Review, Author
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.storage import FileSystemStorage

class BookListView(ListView):
    context_object_name = 'books'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Home | Book Shop"
        context['page_title'] = "Book List"
        return context

    def get_queryset(self):
        return Book.objects.all()
        

class BookDetailView(DetailView):
    model = Book

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        book = context['book']
        context['reviews'] = book.review_set.all().order_by('-created_at')
        context['authors'] = book.authors.all()
        context['title'] = book.title +' | Book Shop'
        context['page_title'] = 'Book Detail Page'
        return context


def index(request):

    bookData = Book.objects.all()
    data = {
            'title': 'Book Shop',
            'page_titie': 'This is a bookshop',
            'books' : bookData
        }
    return render(request, 'books/index.html', data)

def show(request, id):
    singleBook = get_object_or_404(Book, pk=id)
    reviews = Review.objects.filter(book_id=id).order_by('-id')
    data = {
        'title': 'View | Book Shop',
        'page_titie': 'Book Detail Page',
        'book' : singleBook,
        'reviews' : reviews
    }
    return render(request, 'books/show.html', data)

def review(request):

    if request.user.is_authenticated: 
        comment = request.POST['comment']
        book_id = request.POST['book_id']
        newComment = Review(comment=comment, book_id=book_id, user=request.user)

        if len(request.FILES) != 0:

            image = request.FILES['review_image']
            fs = FileSystemStorage()
            name = fs.save(image.name, image)
            newComment.image = fs.url(name)

        newComment.save()
        messages.add_message(request, messages.SUCCESS, 'Successfully submitted')

    return redirect('/books/'+book_id)


def author(request, author):

    books = Book.objects.filter(authors__name=author)
    data = {
        'title': author+' book list | Book Shop',
        'page_titie': 'Books of ' + author,
        'books' : books,
    }
    return render(request, 'books/book_list.html', data)
