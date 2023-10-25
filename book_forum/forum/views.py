from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
    HttpResponse,
)
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.urls import reverse_lazy
from .forms import *
from .services import *
from .models import *
from django.db.models import Count
from .filters import *
from django.core.paginator import Paginator
from django.http import JsonResponse


# Create your views here.
def home(request):
    popular_book = (
        Book.objects.annotate(likes=Count("liked_book")).all().order_by("-views")[:25]
    )
    new_book = (
        Book.objects.annotate(likes=Count("liked_book"))
        .all()
        .order_by("-created_at")[:25]
    )
    popular_discussion = (
        Discussion.objects.annotate(comments=Count("discussion_comments"))
        .all()
        .order_by("-comments")[:25]
    )
    new_discussion = (
        Discussion.objects.annotate(comments=Count("discussion_comments"))
        .all()
        .order_by("-created_at")[:25]
    )
    context = {
        "popular_books": popular_book,
        "popular_discussions": popular_discussion,
        "new_books": new_book,
        "new_discussions": new_discussion,
        "title": "Головна",
    }
    return render(request, template_name="book/home.html", context=context)


def search(request):
    raise (ValueError)
    try:
        type = request.GET["search"][0]
        if type == "#":
            return redirect(
                reverse_lazy(
                    "search_discussions", kwargs={"search": request.GET["search"][1:]}
                )
            )
        else:
            return redirect(
                reverse_lazy("search_books", kwargs={"search": request.GET["search"]})
            )
    except:
        return redirect(reverse_lazy("home"))


def search_books(request, search):
    sort_type = request.GET.get("sort_type", "-")
    sort = request.GET.get("sort", "views")
    sorting_form = SearchBookSort(request.GET)
    filter = SearchBookFilter(
        request.GET,
        queryset=Book.objects.filter(search_title__icontains=search)
        .annotate(
            liked_book_num=Count("liked_book"), disliked_book_num=Count("disliked_book")
        )
        .order_by(f"{sort_type}{sort}"),
    )
    paginator = Paginator(filter.qs, 9)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "type": "book",
        "filter": filter,
        "sorting": sorting_form,
        "page_obj": page_obj,
        "search": search,
        "title": f"Пошук книги {search}",
    }
    return render(request, template_name="book/search.html", context=context)


def search_discussions(request, search):
    sort_type = request.GET.get("sort_type", "-")
    sort = request.GET.get("sort", "views")
    sorting_form = SearchDiscussionSort(request.GET)
    filter = SearchDiscussionFilter(
        request.GET,
        queryset=Discussion.objects.filter(search_title__icontains=search)
        .annotate(
            liked_discussion_num=Count("liked_discussion"),
            disliked_discussion_num=Count("disliked_discussion"),
            comment_discussion_num=Count("discussion_comments"),
        )
        .order_by(f"{sort_type}{sort}"),
    )
    paginator = Paginator(filter.qs, 2)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "type": "discussion",
        "filter": filter,
        "sorting": sorting_form,
        "page_obj": page_obj,
        "search": search,
        "title": f"Пошук обговорення {search}",
    }
    return render(request, template_name="book/search.html", context=context)


# def error500(request):
#     return render(request, template_name='home/home.html')


def catalog(request):
    raise ValueError("BAd rfsdiofoisjoidf")
    categories = get_all_categories()
    context = {
        "categories": categories,
        "title": "Каталог",
    }
    return render(request, template_name="book/catalog.html", context=context)


def category_view(request, category_slug):
    category = get_category_by_slug(category_slug)
    books = get_books_by_category(category)
    paginator = Paginator(books, 9)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "page_obj": page_obj,
        "category": category,
        "title": f"Категорія {category_slug}",
    }
    return render(request, template_name="book/category.html", context=context)


def add_category(request):
    if request.method == "POST":
        form = CreateCategoryForm(request.POST)
        form.save()
        return redirect(reverse_lazy("home"))
    else:
        form = CreateCategoryForm
        return custom_render(
            request,
            "book/add_category.html",
            {"title": "Додати категорію", "form": form},
        )


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
def change_discussion(request, book_slug, discussion_slug):
    book = get_book_by_slug(book_slug)
    discussion = get_discussion_by_book_and_slug(book, discussion_slug)
    if request.user == discussion.user or request.user.is_staff:
        if request.method == "POST":
            return change_discussion_func(request, discussion)
        else:
            form = ChangeDiscussionForm(instance=discussion)
            context = {"form": form, "title": "Додати книгу"}
            return custom_render(request, "book/change_discussion.html", context)
    else:
        redirect(
            "discussion",
            kwargs={"book_slug": book_slug, "discussion_slug": discussion_slug},
        )


@login_required(login_url=reverse_lazy("home"))
def add_book_comment(request, book_slug):
    if request.method == "POST":
        return add_book_comment_func(request, book_slug)


@login_required(login_url=reverse_lazy("home"))
def add_discussion_comment(request, book_slug, discussion_slug):
    book = get_book_by_slug(book_slug)
    discussion = get_discussion_by_book_and_slug(book, discussion_slug)
    if discussion.status == "OP":
        if request.method == "POST":
            return add_discussion_comment_func(request, book, discussion)
    else:
        redirect_to_discussion(book_slug, discussion_slug)


@login_required(login_url=reverse_lazy("home"))
def answer_discussion_comment(request, book_slug, discussion_slug):
    book = get_book_by_slug(book_slug)
    discussion = get_discussion_by_book_and_slug(book, discussion_slug)
    if discussion.status == "OP":
        if request.method == "POST":
            return answer_discussion_comment_func(request, book, discussion)
    else:
        redirect_to_discussion(book_slug, discussion_slug)


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


def handler404(request, *args, **argv):
    response = render(request, "base/404.html", {})
    response.status_code = 404
    return response
