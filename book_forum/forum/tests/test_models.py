
import pytest

from forum.services import *
from forum.models import *
from user.models import *

@pytest.fixture
def category(db):
    return Category.objects.create(title="Horror")

    
@pytest.fixture
def user(db):
    return User.objects.create(
        username="Test",
        email="test@gmail.com", 
        password="1111")

@pytest.fixture
def book(category, user):
    book = Book.objects.create(
        title = "SUPER POOPER BOOK",
        cover = "cover.png",
        description = "lorem ipsum lorem ipsum lorem ipsum lorem ipsum",
        author = "Myke Tyson",
        year = 2013,
        status = "OG",
        user = user
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
        user=user
    )

@pytest.mark.django_db
def test_create_category():
    Category.objects.create(title="Horror")
    assert Category.objects.count() == 1