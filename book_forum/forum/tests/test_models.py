import pytest

from forum.models import *
from user.models import *


@pytest.fixture
def user_password():
    return "fhgsdfhgszdfgsa"


@pytest.fixture
def category(db):
    return Category.objects.create(title="Horror")


@pytest.fixture
def user(db):
    return User.objects.create(username="Test", email="test@gmail.com", password=user_password)


@pytest.fixture
def logged_in_client(client, user):
    client.force_login(user)
    return client


@pytest.fixture
def book(category, user):
    book = Book.objects.create(
        title="test1",
        cover="cover.png",
        description="lorem ipsum lorem ipsum lorem ipsum lorem ipsum",
        author="Myke Tyson",
        year=2013,
        status="OG",
        user=user,
    )
    book.category.set([category])
    return book


@pytest.fixture
def discussion(book, user):
    discussion = Discussion.objects.create(
        title="IS this book interesting?",
        description="Write your opinion",
        status="OP",
        book=book,
        user=user,
    )
    return discussion
