""" view definitions for api app """

from rest_framework import generics

from books.models import Book
from .serializers import BookSerializer


class BookAPIView(generics.ListAPIView):
    """ API list view definition """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
