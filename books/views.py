from django.views.generic import ListView, DetailView

from .models import Book


class BooksListView(ListView):
    model = Book
    template_name = "books_list.html"
    context_object_name = "books"


class BooksDetailView(DetailView):
    model = Book
    template_name = "books_detail.html"
    context_object_name = "book"
