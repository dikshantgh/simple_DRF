# api/serializers.py
from rest_framework import serializers

from books.models import Book


class BookSerializer(serializers.ModelSerializer):
#     modules = ModuleSerializer(many=True, read_only=True)
# 	  subject = serializers.SlugRelatedField(read_only=True, slug_field='title')

    class Meta:
        model = Book
        fields = ('title', 'subtitle', 'author', 'isbn',)


