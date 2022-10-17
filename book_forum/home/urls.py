from django.urls import path

from .views import *

urlpatterns = [
    path('search_discussions/<search>/', search_discussions , name="search_discussions"),
    path('search_books/<search>/', search_books, name="search_books"),
    path('search/', search, name="search"),
    path('home/', home, name="home"),
    path('', home, name="home"),
]