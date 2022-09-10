from django.urls import path

from .views import *

urlpatterns = [
    path('<book_id>', book , name="book"),
    path('<book_id>/change_book/', discussion , name="discussion"),
    path('<book_id>/discussion/<discussion_id>', discussion , name="discussion"),
    path('<book_id>/discussion/<discussion_id>/change_discussion', discussion , name="discussion"),
    path('category/', category , name="category"),
    path('add_book/', add_book , name="add_book"),
    path('<book_id>/add_discussion/', add_discussion , name="add_discussion"),
]