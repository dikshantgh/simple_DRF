from django.shortcuts import render
from rest_framework.generics import ListAPIView

from api.serializers import BookSerializer
from books.models import Book


class BookAPIView(ListAPIView):
    # ListAPIView to create a read-only endpoint for all book instances
    queryset = Book.objects.all()
    # Its main purpose is to save the state of an object in order to be able to recreate it when needed They're used
    # to convert the data sent in a HTTP request to a Django object and a Django object to a valid response data.
    # A serializer translates data into a format that is easy to consume over the internet,
    # typically JSON, and is displayed at an API endpoint.
    serializer_class = BookSerializer
