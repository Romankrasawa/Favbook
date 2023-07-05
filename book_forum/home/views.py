from django.shortcuts import render, redirect
from forum.models import *
from django.db.models import Count
from .filters import *
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.urls import reverse_lazy
import logging
from django.contrib import messages
from .services import *

logger = logging.getLogger(__name__)


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
    return render(request, template_name="home/home.html", context=context)


def search(request):
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
    sort_type = request.GET.get('sort_type', '-')
    sort = request.GET.get('sort', 'views')
    sorting_form = SearchBookSort(request.GET)
    filter = SearchBookFilter(
        request.GET, queryset=Book.objects.filter(
            search_title__icontains=search
            ).annotate(
                liked_book_num=Count('liked_book'),
                disliked_book_num=Count('disliked_book')
            ).order_by(f"{sort_type}{sort}")
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
    print(filter.qs)
    return render(request, template_name="home/search.html", context=context)


def search_discussions(request, search):
    filter = SearchDiscussionFilter(
        request.GET, queryset=Discussion.objects.filter(search_title__icontains=search)
    )
    paginator = Paginator(filter.qs, 2)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "type": "discussion",
        "filter": filter,
        "page_obj": page_obj,
        "search": search,
        "title": f"Пошук обговорення {search}",
    }
    print(filter.qs)
    return render(request, template_name="home/search.html", context=context)


# def error500(request):
#     return render(request, template_name='home/home.html')
