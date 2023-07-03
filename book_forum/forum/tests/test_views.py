import pytest
from django.test import Client
from forum.services import *
from forum.models import *
from django.urls import reverse_lazy


@pytest.mark.django_db
def test_home(client):
    response = client.get(reverse_lazy("home"))
    assert response.status_code == 200
