import pytest
from django.test import Client
from forum.services import *
from .test_models import *
from django.urls import reverse_lazy


@pytest.mark.django_db
def test_home(client):
    response = client.get(reverse_lazy("home"))
    assert response.status_code == 200

@pytest.mark.django_db
def test_book(client, book):
    response = client.get(reverse_lazy("book", kwargs={"book_slug": book.slug}))
    assert response.status_code == 200

@pytest.mark.django_db
def test_discussion(client, book, discussion):
    response = client.get(reverse_lazy("discussion", kwargs={"book_slug": discussion.book.slug, "discussion_slug":discussion.slug}))
    assert response.status_code == 200

@pytest.mark.django_db
def test_books(logged_in_client):
    response = logged_in_client.get(reverse_lazy("books"))
    assert response.status_code == 200

@pytest.mark.django_db
def test_discussions(logged_in_client):
    response = logged_in_client.get(reverse_lazy("discussions"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_add_book_get(logged_in_client):
    response = logged_in_client.get(reverse_lazy("add_book"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_add_book_post(logged_in_client, category, book):
    data = {
        "title":"tesstgg2",
        "cover":"cover.png",
        "author":"tesgggt",
        "description":"ddddds",
        "year":1111,
        "status":"OG",
        "category": category.pk
    }
    response = logged_in_client.post(reverse_lazy("add_book"), data)
    assert response.status_code == 302


# @pytest.mark.django_db
# def test_add_discussion_get(logged_in_client):
#     response = logged_in_client.get(reverse_lazy("add_discussion"))
#     assert response.status_code == 200


@pytest.mark.django_db
def test_add_discussion_post(logged_in_client, book):
    data = {
        "title":"testdiscus",
        "description":"test",
        "author":"test",
        "status":"OP",
        "book":book.title
    }
    response = logged_in_client.post(reverse_lazy("add_discussion"), json=data)
    assert response.status_code in [200, 302]