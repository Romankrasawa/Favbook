from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.db.models import Q
from django.urls import reverse_lazy
from .forms import *
from .models import *
import logging

logger = logging.getLogger(__name__)

def get_book_by_slug(slug:str) -> Book:
    return get_object_or_404(Book, slug=slug)

def get_discussion_by_book_and_slug(book:Book, discussion_slug:str) -> Discussion:
    return get_object_or_404(Discussion, Q(slug=discussion_slug) & Q(book = book))


def increase_book_views(book: Book) -> None:
    book.views += 1
    book.save()

def get_all_books_created_by_user(request:HttpResponse) -> Book | None:
    return request.user.user_book.all()

def get_all_books_liked_by_user(request:HttpResponse) -> Book | None:
    return request.user.liked_book.all()

def get_all_books_disliked_by_user(request:HttpResponse) -> Book | None:
    return request.user.disliked_book.all()

def get_info_about_fav_user_books(
        request:HttpResponse
        ) -> tuple[Book | None, Book | None, Book | None]:
    created_books = get_all_books_created_by_user(request)
    liked_books = get_all_books_liked_by_user(request)
    disliked_books = get_all_books_disliked_by_user(request)
    return created_books,liked_books,disliked_books

def get_all_discussions_created_by_user(request:HttpResponse) -> Discussion | None:
    return request.user.user_discussion.all()

def get_all_discussions_liked_by_user(request:HttpResponse) -> Discussion | None:
    return request.user.liked_discussion.all()

def get_all_discussions_disliked_by_user(request:HttpResponse) -> Discussion | None:
    return request.user.disliked_discussion.all()

def get_info_about_fav_user_discussions(
        request:HttpResponse
        ) -> tuple[Discussion | None, Discussion | None, Discussion | None]:
    created_discussions = get_all_discussions_created_by_user(request)
    liked_discussions = get_all_discussions_liked_by_user(request)
    disliked_discussions = get_all_discussions_disliked_by_user(request)
    return created_discussions,liked_discussions,disliked_discussions

def is_form_valid(form) -> bool:
    return form.is_valid() and form.is_multipart()

def create_book(request:HttpResponse, form)  -> HttpResponse:
    category = form.cleaned_data['category']
    form.cleaned_data.pop("category", None)
    book = Book.objects.create(**form.cleaned_data, user = request.user)
    book.category.set(category)
    return redirect(book.get_absolute_url())

def add_book_func(request:HttpResponse) -> HttpResponse:
    form = CreateBookForm(request.POST, request.FILES)
    if is_form_valid(form):
        return create_book(request, form)
    else:
        return redirect(reverse_lazy("add_book"))
    