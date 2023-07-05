import django_filters
from forum.models import *
from django.db import models
from django import forms


class Status(models.TextChoices):
    ONGOING = "OG", "Виходить"
    FINISHED = "FN", "Закінчене"


class SearchBookFilter(django_filters.FilterSet):
    views = django_filters.NumberFilter(
        field_name="views",
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "Книга",
                "autocomplete": "off",
            }
        ),
        label="Перегляди",
    )
    views_min = django_filters.NumberFilter(
        field_name="views",
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "Книга",
                "autocomplete": "off",
            }
        ),
        label="Мінімальна кількість переглядів",
        lookup_expr="gte",
    )
    views_max = django_filters.NumberFilter(
        field_name="views",
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "Книга",
                "autocomplete": "off",
            }
        ),
        label="Максимальна кількість переглядів",
        lookup_expr="lte",
    )

    year = django_filters.NumberFilter(
        field_name="year",
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "Книга",
                "autocomplete": "off",
            }
        ),
        label="Рік",
    )
    year_min = django_filters.NumberFilter(
        field_name="year",
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "Книга",
                "autocomplete": "off",
            }
        ),
        label="Мінімальний рік",
        lookup_expr="gte",
    )
    year_max = django_filters.NumberFilter(
        field_name="year",
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "Книга",
                "autocomplete": "off",
            }
        ),
        label="Максимальний рік",
        lookup_expr="lte",
    )

    status = django_filters.ChoiceFilter(
        field_name="status",
        choices=Status.choices,
        widget=forms.Select(
            attrs={
                "class": "form-control",
                "placeholder": "Книга",
                "autocomplete": "off",
            }
        ),
        label="Статус",
    )

    category = django_filters.ModelMultipleChoiceFilter(
        field_name="category",
        queryset=Category.objects.all(),
        widget=forms.SelectMultiple(
            attrs={
                "class": "form-control",
                "placeholder": "Книга",
                "autocomplete": "off",
            }
        ),
        label="Категорії",
    )

    class Meta:
        model = Book
        fields = ["views", "year", "status", "category"]


class SearchDiscussionFilter(django_filters.FilterSet):
    class Status(models.TextChoices):
        OPENED = "OP", "Відкрите"
        CLOSED = "CL", "Закрите"

    # comments = django_filters.NumberFilter(field_name='comments', widget = forms.NumberInput(attrs={"class": "form-control", 'placeholder':'Книга', 'autocomplete':'off'}), label='Коментарі')
    # comments_min = django_filters.NumberFilter(field_name='comments', widget = forms.NumberInput(attrs={"class": "form-control", 'placeholder':'Книга', 'autocomplete':'off'}), label='Мінімальна кількість коментарів', lookup_expr='gte')
    # comments_max = django_filters.NumberFilter(field_name='comments', widget = forms.NumberInput(attrs={"class": "form-control", 'placeholder':'Книга', 'autocomplete':'off'}), label='Максимальна кількість коментарів', lookup_expr='lte')

    status = django_filters.ChoiceFilter(
        field_name="status",
        choices=Status.choices,
        widget=forms.Select(
            attrs={
                "class": "form-control",
                "placeholder": "Книга",
                "autocomplete": "off",
            }
        ),
        label="Статус",
    )

    book = django_filters.ModelMultipleChoiceFilter(
        field_name="book",
        queryset=Book.objects.all(),
        widget=forms.SelectMultiple(
            attrs={
                "class": "form-control",
                "placeholder": "Книга",
                "autocomplete": "off",
            }
        ),
        label="Книги",
    )

    class Meta:
        model = Discussion
        fields = ["status", "book"]


class SearchBookSort(forms.Form):
    class Sorts(models.TextChoices):
        VIEWS = "views", "Перегляди"
        YEAR = "year", "Роки"
        TITLE = "title", "Назви"

    class Sorts_types(models.TextChoices):
        DOWN = "-", "Спадання"
        UP = "", "Зростання"

    sort = forms.CharField(
        widget=forms.Select(
            attrs={
                "value": "views",
                "class": "form-control",
                "placeholder": "Книга",
                "autocomplete": "off",
            },
            choices=Sorts.choices,
        )
    )
    sort_type = forms.CharField(
        widget=forms.Select(
            attrs={
                "value":"-",
                "class": "form-control",
                "placeholder": "Книга",
                "autocomplete": "off",
            },
            choices=Sorts_types.choices,
        )
    )
