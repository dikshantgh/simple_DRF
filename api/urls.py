# ap1/urls.py
"""This is the url route for api app"""
from django.urls import path

from api import views

urlpatterns = [
    path('', views.BookAPIView.as_view()),
]