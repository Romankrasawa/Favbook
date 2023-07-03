from django.db import models
from django.contrib.postgres.fields import ArrayField, HStoreField
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from slugify import slugify
from django.urls import reverse_lazy
import uuid
import os
from django.conf import settings

from forum.models import *


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not username:
            raise ValueError("Користувач повинен мати імя")
        if not email:
            raise ValueError("Користувач повинен мати електронну пошту")
        user = self.model(email=self.normalize_email(email), username=username)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email=email,
            username=username,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)


def photo_file_name(self, filename):
    return f"photos/{self.pk}/{filename}"


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = models.SlugField(blank=True)
    username = models.CharField(max_length=30, verbose_name="Імя", unique=True)
    email = models.EmailField(
        max_length=70, verbose_name="Електронна Пошта", unique=True
    )
    photo = models.ImageField(
        upload_to=photo_file_name,
        default="default/default_avatar.png",
        verbose_name="Фото",
    )
    is_superuser = models.BooleanField(default=False, verbose_name="Адміністратор")
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True, verbose_name="Активовано")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Створено")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Оновлено")
    liked_book = models.ManyToManyField(
        Book, related_name="liked_book", verbose_name="Вподобані книги"
    )
    disliked_book = models.ManyToManyField(
        Book, related_name="disliked_book", verbose_name="Невподобані книги"
    )
    liked_discussion = models.ManyToManyField(
        Discussion, related_name="liked_discusion", verbose_name="Вподобані обговорення"
    )
    disliked_discussion = models.ManyToManyField(
        Discussion,
        related_name="disliked_discusion",
        verbose_name="Невподобані обговорення",
    )

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    @property
    def get_liked_book(self):
        return [book.title for book in self.liked_book.all()]

    get_liked_book.fget.short_description = "Вподобані книги"

    @property
    def get_disliked_book(self):
        return [book.title for book in self.disliked_book.all()]

    get_disliked_book.fget.short_description = "Невподобані книги"

    @property
    def get_liked_discussion(self):
        return [discussion.title for discussion in self.liked_discussion.all()]

    get_liked_discussion.fget.short_description = "Вподобані обговорення"

    @property
    def get_disliked_discussion(self):
        return [discussion.title for discussion in self.disliked_discussion.all()]

    get_disliked_discussion.fget.short_description = "Невподобані обговорення"

    @property
    def get_liked_discussion_comment(self):
        return [
            discussion_comment.title
            for discussion_comment in self.liked_discussion_comment.all()
        ]

    get_liked_discussion_comment.fget.short_description = "Вподобані коментарі"

    @property
    def get_disliked_discussion_comment(self):
        return [
            discussion_comment.title
            for discussion_comment in self.disliked_discussion_comment.all()
        ]

    get_disliked_discussion_comment.fget.short_description = "Невподобані коментарі"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super(User, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.photo))
        super().delete(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy("profile", kwargs={"user_slug": self.slug})

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Користувач"
        verbose_name_plural = "Користувачі"
