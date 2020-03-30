# books/urls.py

"""This is the url route for books app"""
from django.urls import path

from books import views

urlpatterns = [
    path('', views.BookListView.as_view(), name='book_list'),
]