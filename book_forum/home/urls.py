from django.urls import path

from .views import *

urlpatterns = [
    path('', home , name="home"),
    path('home/', home , name="home"),
    path('search/', search , name="search"),
    path('search_profiles/', search_profiles , name="search_profiles"),
    path('search_books/', search_books , name="search_books"),
    path('search_discussions/', search_discussions , name="search_discussions"),
    path('news/', news , name="news"),
]