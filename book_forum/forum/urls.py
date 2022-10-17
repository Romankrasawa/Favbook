from django.urls import path

from .views import *

urlpatterns = [
    path('<slug:book_id>/discussion/<slug:discussion_id>/add_comment', add_discussion_comment, name="add_discussion_comment"),
    path('<slug:book_id>/discussion/<slug:discussion_id>/answer_comment', answer_discussion_comment,name="answer_discussion_comment"),
    path('<slug:book_id>/discussion/<slug:discussion_id>/dislike', dislike_discussion, name="dislike_discussion"),
    path('<slug:book_id>/discussion/<slug:discussion_id>/like', like_discussion, name="like_discussion"),
    path('<slug:book_id>/discussion/<slug:discussion_id>/', discussion, name="discussion"),
    path('<slug:book_id>/add_discussion/', add_concrete_discussion , name="add_concrete_discussion"),
    path('add_discussion/', add_discussion, name="add_discussion"),
    path('discussion/', discussions, name="discussions"),
    path('add_book/', add_book, name="add_book"),
    path('<slug:book_id>/add_comment/', add_book_comment, name="add_book_comment"),
    path('<slug:book_id>/dislike', dislike_book, name="dislike_book"),
    path('<slug:book_id>/like', like_book, name="like_book"),
    path('<slug:book_id>/', book, name="book"),
    path('', books, name="books"),
]