""" Model registrations for books app """
from django.contrib import admin

from .models import Book

admin.site.register(Book)
