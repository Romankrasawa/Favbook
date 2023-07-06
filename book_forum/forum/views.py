from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.urls import reverse_lazy
from .forms import *
from .models import *
from .services import *


def book(request, book_slug):
    book = get_book_by_slug(book_slug)
    increase_book_views(book)
    form = CreateBook_commentForm
    context = {"form": form, "book": book, "title": f"Книга {book.title}"}
    return render(request, template_name="book/book.html", context=context)


@login_required(login_url=reverse_lazy("home"))
def books(request):
    books_info = get_info_about_fav_user_books(request)
    created_book, liked_book, disliked_book = books_info
    context = {
        "created_book": created_book,
        "liked_book": liked_book,
        "disliked_book": disliked_book,
        "title": "Книги",
    }
    return render(request, template_name="book/books.html", context=context)


def discussion(request, book_slug, discussion_slug):
    book = get_book_by_slug(book_slug)
    discussion = get_discussion_by_book_and_slug(book, discussion_slug)
    increase_discussion_views(discussion)
    form = CreateDiscussion_commentForm
    answerform = AnswerDiscussion_commentForm
    context = {
        "form": form,
        "answerform": answerform,
        "book": book,
        "discussion": discussion,
        "title": f"Обговорення {discussion.title}",
    }
    return render(request, template_name="book/discussion.html", context=context)


@login_required(login_url=reverse_lazy("home"))
def discussions(request):
    discussions_info = get_info_about_fav_user_discussions(request)
    created_discussion, liked_discussion, disliked_discussion = discussions_info
    context = {
        "created_discussion": created_discussion,
        "liked_discussion": liked_discussion,
        "disliked_discussion": disliked_discussion,
        "title": "Обговорення",
    }
    return render(request, template_name="book/discussions.html", context=context)


@login_required(login_url=reverse_lazy("home"))
def add_book(request):
    if request.method == "POST":
        return add_book_func(request)
    else:
        form = CreateBookForm
        context = {"form": form, "title": "Додати книгу"}
        return custom_render(request, "book/add_book.html", context)


@login_required(login_url=reverse_lazy("home"))
def change_book(request, book_slug):
    book = get_book_by_slug(book_slug)
    if request.user == book.user or request.user.is_staff:
        if request.method == "POST":
            return change_book_func(request, book)
        else:
            form = ChangeBookForm(instance=book)
            context = {"form": form, "title": "Додати книгу", "book": book}
            return custom_render(request, "book/change_book.html", context)
    else:
        redirect("book", kwargs={"book_slug": book_slug})


@login_required(login_url=reverse_lazy("home"))
def add_discussion(request):
    if request.method == "POST":
        return add_discussion_func(request)
    else:
        form = CreateDiscussionForm()
        context = {"form": form, "title": f"Додати обговорення"}
        return custom_render(request, "book/add_discussion.html", context)


@login_required(login_url=reverse_lazy("home"))
def add_concrete_discussion(request, book_slug):
    book = get_book_by_slug(book_slug)
    form = CreateDiscussionForm(initial={"book": book})
    return render(
        request,
        template_name="book/add_discussion.html",
        context={"form": form, "title": "Додати обговорення"},
    )


@login_required(login_url=reverse_lazy("home"))
def add_discussion_comment(request, book_slug, discussion_slug):
    if request.method == "POST":
        return add_discussion_comment_func(request, book_slug, discussion_slug)


@login_required(login_url=reverse_lazy("home"))
def add_book_comment(request, book_slug):
    if request.method == "POST":
        return add_book_comment_func(request, book_slug)


@login_required(login_url=reverse_lazy("home"))
def answer_discussion_comment(request, book_slug, discussion_slug):
    if request.method == "POST":
        return answer_discussion_comment_func(request, book_slug, discussion_slug)


@login_required(login_url=reverse_lazy("home"))
def like_book(request, book_slug):
    return like_book_func(request, book_slug)


@login_required(login_url=reverse_lazy("home"))
def dislike_book(request, book_slug):
    return dislike_book_func(request, book_slug)


@login_required(login_url=reverse_lazy("home"))
def like_discussion(request, book_slug, discussion_slug):
    return like_discussion_func(request, book_slug, discussion_slug)


@login_required(login_url=reverse_lazy("home"))
def dislike_discussion(request, book_slug, discussion_slug):
    return dislike_discussion_func(request, book_slug, discussion_slug)
