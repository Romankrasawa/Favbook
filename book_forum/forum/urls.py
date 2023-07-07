from django.urls import path

from .views import *

urlpatterns = [
    path(
        "book/<slug:book_slug>/discussion/<slug:discussion_slug>/change_discussion/",
        change_discussion,
        name="change_discussion",
    ),
    path(
        "book/<slug:book_slug>/discussion/<slug:discussion_slug>/add_comment",
        add_discussion_comment,
        name="add_discussion_comment",
    ),
    path(
        "book/<slug:book_slug>/discussion/<slug:discussion_slug>/answer_comment",
        answer_discussion_comment,
        name="answer_discussion_comment",
    ),
    path(
        "book/<slug:book_slug>/discussion/<slug:discussion_slug>/dislike",
        dislike_discussion,
        name="dislike_discussion",
    ),
    path(
        "book/<slug:book_slug>/discussion/<slug:discussion_slug>/like",
        like_discussion,
        name="like_discussion",
    ),
    path(
        "book/<slug:book_slug>/discussion/<slug:discussion_slug>/",
        discussion,
        name="discussion",
    ),
    path(
        "book/<slug:book_slug>/add_discussion/",
        add_concrete_discussion,
        name="add_concrete_discussion",
    ),
    path("book/add_discussion/", add_discussion, name="add_discussion"),
    path("book/discussion/", discussions, name="discussions"),
    path("book/add_book/", add_book, name="add_book"),
    path("book/<slug:book_slug>/change_book/", change_book, name="change_book"),
    path(
        "book/<slug:book_slug>/add_comment/", add_book_comment, name="add_book_comment"
    ),
    path("book/<slug:book_slug>/dislike", dislike_book, name="dislike_book"),
    path("book/<slug:book_slug>/like", like_book, name="like_book"),
    path("book/<slug:book_slug>/", book, name="book"),
    path("book/", books, name="books"),
    path("search_discussions/<search>/", search_discussions, name="search_discussions"),
    path("search_books/<search>/", search_books, name="search_books"),
    path("category/<slug:category_slug>", category_view, name="category"),
    path("catalog/", catalog, name="catalog"),
    path("search/", search, name="search"),
    path("home/", home, name="home"),
    path("", home, name="home"),
]
