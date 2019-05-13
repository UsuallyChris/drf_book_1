""" View definitions for books app """
from django.views.generic import ListView

from .models import Book


class BookListView(ListView):
    """ BookListView config """
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'
