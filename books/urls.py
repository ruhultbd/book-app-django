from django.urls import path

from . import views
from books.views import BookListView, BookDetailView

urlpatterns = [
    path('', BookListView.as_view(), name='index'),
    path('<int:pk>', BookDetailView.as_view(), name='book.show'),
    path('review', views.review, name='book.review'),
    path('<str:author>', views.author, name='author.books')
]