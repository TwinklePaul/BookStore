from django.urls import path

from .views import BooksListView, BooksDetailView

urlpatterns = [
    path("", BooksListView.as_view(), name="books"),
    path("<uuid:pk>", BooksDetailView.as_view(), name="book_details")
]
