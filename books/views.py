from django.shortcuts import render
from django.views.generic import ListView
from .models import Book  # Assuming you have a Book model in your models.py

class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'  # Assuming you have a template named 'book_list.html'
    context_object_name = 'books'  # Optional: Specify the context variable name for the queryset
