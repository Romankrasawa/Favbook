from django.conf import settings
from django.db import models
from django.db.models import Count
from slugify import slugify
from django.urls import reverse_lazy
import uuid
import logging

logger = logging.getLogger(__name__)


def covers_file_name(self, filename):
    return f"covers/{self.pk}/{filename}"


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = models.SlugField(blank=True)
    title = models.CharField(max_length=100, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"


class Book(models.Model):
    class Status(models.TextChoices):
        ONGOING = "OG", "Виходить"
        FINISHED = "FN", "Закінчене"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = models.SlugField(blank=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Користувач",
        related_name="user_book",
    )
    title = models.CharField(max_length=100, verbose_name="Назва", unique=True)
    search_title = models.CharField(max_length=100)
    description = models.TextField(max_length=2000, verbose_name="Опис")
    author = models.CharField(max_length=100, verbose_name="Автор")
    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.ONGOING,
        verbose_name="Статус",
    )
    year = models.IntegerField(verbose_name="Рік")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Створено")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Оновлено")
    category = models.ManyToManyField(Category, verbose_name="Жанри")
    cover = models.ImageField(
        upload_to=covers_file_name,
        verbose_name="Обкладинка",
        default="default/default_cover.jpg",
    )
    views = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        self.search_title = self.title.lower()
        super(Book, self).save(*args, **kwargs)

    @property
    def get_category(self):
        return [discussion.title for discussion in self.category.all()]

    get_category.fget.short_description = "Категорії"

    def get_absolute_url(self):
        return reverse_lazy("book", kwargs={"book_slug": self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"


class Book_comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        verbose_name="Книга",
        null=True,
        related_name="book_comments",
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Користувач"
    )

    content = models.TextField(max_length=2000, verbose_name="Зміст коментаря")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата")

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = "Коментар книги"
        verbose_name_plural = "Коментарі книги"
        ordering = [
            "-created_at",
        ]


class Discussion(models.Model):
    class Status(models.TextChoices):
        OPENED = "OP", "Відкрите"
        CLOSED = "CL", "Закрите"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = models.SlugField(blank=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Користувач",
        related_name="user_discussion",
    )
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        verbose_name="Книга",
        related_name="discussion_book",
    )
    title = models.CharField(max_length=100, verbose_name="Назва", unique=True)
    search_title = models.CharField(max_length=100)
    description = models.TextField(max_length=2000, verbose_name="Опис")
    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.OPENED,
        verbose_name="Статус",
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Створено")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Оновлено")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        self.search_title = self.title.lower()
        super(Discussion, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy(
            "discussion",
            kwargs={"book_slug": self.book.slug, "discussion_slug": self.slug},
        )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Обговорення"
        verbose_name_plural = "Обговорення"


class Discussion_comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    discussion = models.ForeignKey(
        Discussion,
        on_delete=models.CASCADE,
        verbose_name="Обговорення",
        null=True,
        related_name="discussion_comments",
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Користувач"
    )

    answer = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Відповідь на",
        related_name="discussion_answer",
    )
    content = models.TextField(max_length=2000, verbose_name="Зміст коментаря")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата")

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = "Коментар обговорення"
        verbose_name_plural = "Коментарі обговорення"
        ordering = [
            "-created_at",
        ]
