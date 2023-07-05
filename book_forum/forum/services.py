from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.db.models import Q
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import *
from .models import *
import logging

logger = logging.getLogger(__name__)


def custom_render(request:HttpResponse, template_name:str, context:dict) -> HttpResponse:
    return render(request, template_name=template_name, context=context)


def redirect_to_discussion(book_slug: str, discussion_slug: str) -> HttpResponse:
    return redirect(
        reverse_lazy(
            "discussion",
            kwargs={"book_slug": book_slug, "discussion_slug": discussion_slug},
        )
    )


def get_book_by_slug(slug: str) -> Book:
    logger.error("error")
    return get_object_or_404(Book, slug=slug)


def get_discussion_by_book_and_slug(book: Book, discussion_slug: str) -> Discussion:
    return get_object_or_404(Discussion, Q(slug=discussion_slug) & Q(book=book))


def get_discussion_comment_by_id(discussion_comment_id: str) -> Discussion_comment:
    return get_object_or_404(Discussion_comment, id=discussion_comment_id)

def increase_book_views(book: Book) -> None:
    book.views += 1
    book.save()


def get_all_books_created_by_user(request: HttpResponse) -> Book | None:
    return request.user.user_book.all()


def get_all_books_liked_by_user(request: HttpResponse) -> Book | None:
    return request.user.liked_book.all()


def get_all_books_disliked_by_user(request: HttpResponse) -> Book | None:
    return request.user.disliked_book.all()


def get_info_about_fav_user_books(
    request: HttpResponse,
) -> tuple[Book | None, Book | None, Book | None]:
    created_books = get_all_books_created_by_user(request)
    liked_books = get_all_books_liked_by_user(request)
    disliked_books = get_all_books_disliked_by_user(request)
    return created_books, liked_books, disliked_books


def get_all_discussions_created_by_user(request: HttpResponse) -> Discussion | None:
    return request.user.user_discussion.all()


def get_all_discussions_liked_by_user(request: HttpResponse) -> Discussion | None:
    return request.user.liked_discussion.all()


def get_all_discussions_disliked_by_user(request: HttpResponse) -> Discussion | None:
    return request.user.disliked_discussion.all()


def get_info_about_fav_user_discussions(
    request: HttpResponse,
) -> tuple[Discussion | None, Discussion | None, Discussion | None]:
    created_discussions = get_all_discussions_created_by_user(request)
    liked_discussions = get_all_discussions_liked_by_user(request)
    disliked_discussions = get_all_discussions_disliked_by_user(request)
    return created_discussions, liked_discussions, disliked_discussions


def is_form_valid(form) -> bool:
    return form.is_valid()


def create_book(request: HttpResponse, form:CreateBookForm) -> HttpResponse:
    category = form.cleaned_data["category"]
    form.cleaned_data.pop("category", None)
    book = Book.objects.create(**form.cleaned_data, user=request.user)
    book.category.set(category)
    messages.add_message(request, messages.SUCCESS, "Книга була успішно створена.")
    return redirect(book.get_absolute_url())


def add_book_func(request: HttpResponse) -> HttpResponse:
    form = CreateBookForm(request.POST, request.FILES)
    if is_form_valid(form):
        return create_book(request, form)
    else:
        messages.add_message(request, messages.ERROR, "Книгу не було створено.")
        context = {"form": form, "title": "Додати книгу"}
        return custom_render(request, "book/add_book.html", context)

def create_discussion(request: HttpResponse, form: CreateDiscussionForm) -> HttpResponse:
    discussion = Discussion.objects.create(**form.cleaned_data, user=request.user)
    messages.add_message(request, messages.SUCCESS, "Обговорення було успішно створено.")
    return redirect(discussion.get_absolute_url())


def add_discussion_func(request: HttpResponse) -> HttpResponse:
    form = CreateDiscussionForm(request.POST)
    if is_form_valid(form):
        return create_discussion(request, form)
    else:
        messages.add_message(request, messages.ERROR, "Обговорення не було створено.")
        context={"form": form, "title": f"Додати обговорення"}
        return custom_render(request, "book/add_discussion.html", context)


def create_book_comment(request:HttpResponse, form:CreateBook_commentForm, book: Book) -> None:
    Book_comment.objects.create(
        **form.cleaned_data, user=request.user, book=book
    )


def add_book_comment_func(request: HttpResponse, book_slug: str) -> HttpResponse:
    book = get_book_by_slug(book_slug)
    form = CreateBook_commentForm(request.POST)
    if is_form_valid(form):
        logger.debug("okey")
        create_book_comment(request, form, book)
        messages.add_message(request, messages.SUCCESS, "Ваш коментар опубліковано.")
        return redirect(reverse_lazy("book", kwargs={"book_slug": book_slug}))
    else:
        messages.add_message(request, messages.ERROR, "Ваш коментар не було опубліковано.")
        return redirect(reverse_lazy("book", kwargs={"book_slug": book_slug}))


def create_discussion_comment(request:HttpResponse,
    form:CreateDiscussion_commentForm,
    discussion: Discussion, 
    answer: Discussion = None) -> None:
    Discussion_comment.objects.create(
            **form.cleaned_data, user=request.user, discussion=discussion, answer=answer
        )


def add_discussion_comment_func(request: HttpResponse, book_slug: str, discussion_slug: str) -> HttpResponse:
    book = get_book_by_slug(book_slug)
    discussion = get_discussion_by_book_and_slug(book, discussion_slug)
    form = CreateDiscussion_commentForm(request.POST)
    if is_form_valid(form):
        create_discussion_comment(request, form, discussion)
        messages.add_message(request, messages.SUCCESS, "Ваш коментар опубліковано.")
        return redirect_to_discussion(book_slug, discussion_slug)
    else:
        messages.add_message(request, messages.ERROR, "Ваш коментар не було опубліковано.")
        redirect_to_discussion(book_slug, discussion_slug)


def answer_discussion_comment_func(request: HttpResponse, book_slug: str, discussion_slug: str) -> HttpResponse:
    book = get_book_by_slug(book_slug)
    discussion = get_discussion_by_book_and_slug(book, discussion_slug)
    answer_id = request.POST.get("answer")
    answer = get_discussion_comment_by_id(answer_id)
    content = request.POST.get("content")
    form = AnswerDiscussion_commentForm(request.POST)
    logger.debug(answer)
    if is_form_valid(form):
        form.cleaned_data.pop("answer")
        create_discussion_comment(request, form, discussion, answer)
        messages.add_message(request, messages.SUCCESS, "Ваш коментар опубліковано.")
        return redirect_to_discussion(book_slug, discussion_slug)
    else:
        messages.add_message(request, messages.ERROR, "Ваш коментар не було опубліковано.")
        redirect_to_discussion(book_slug, discussion_slug)


def like_book_func(request: HttpResponse, book_slug: str) -> HttpResponse:
    book = get_book_by_slug(book_slug)
    if book in request.user.disliked_book.all():
        request.user.disliked_book.remove(book)
        request.user.liked_book.add(book)
    else:
        request.user.liked_book.add(book)
    return HttpResponse(200)


def dislike_book_func(request: HttpResponse, book_slug: str) -> HttpResponse:
    book = get_book_by_slug(book_slug)
    if book in request.user.liked_book.all():
        request.user.liked_book.remove(book)
        request.user.disliked_book.add(book)
    else:
        request.user.disliked_book.add(book)
    return HttpResponse(200)


def like_discussion_func(request: HttpResponse, book_slug: str, discussion_slug: str) -> HttpResponse:
    book = get_book_by_slug(book_slug)
    discussion = get_discussion_by_book_and_slug(book, discussion_slug)
    if discussion in request.user.disliked_discussion.all():
        request.user.disliked_discussion.remove(discussion)
        request.user.liked_discussion.add(discussion)
    else:
        request.user.liked_discussion.add(discussion)
    return HttpResponse(200)


def dislike_discussion_func(request: HttpResponse, book_slug: str, discussion_slug: str) -> HttpResponse:
    book = get_book_by_slug(book_slug)
    discussion = get_discussion_by_book_and_slug(book, discussion_slug)
    if discussion in request.user.liked_discussion.all():
        request.user.liked_discussion.remove(discussion)
        request.user.disliked_discussion.add(discussion)
    else:
        request.user.disliked_discussion.add(discussion)
    return HttpResponse(200)