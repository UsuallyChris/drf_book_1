""" serializer definitions for api app """
from rest_framework import serializers

from books.models import Book


class BookSerializer(serializers.ModelSerializer):
    """ docstring """
    class Meta:
        model = Book
        fields = ('title', 'subtitle', 'author', 'isbn')
