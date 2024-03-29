# Generated by Django 4.2.1 on 2023-06-30 12:55

from django.db import migrations, models
import user.models
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("forum", "0001_initial"),
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("slug", models.SlugField(blank=True)),
                (
                    "username",
                    models.CharField(max_length=30, unique=True, verbose_name="Імя"),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=70, unique=True, verbose_name="Електронна Пошта"
                    ),
                ),
                ("token", models.UUIDField(default=uuid.uuid4)),
                (
                    "photo",
                    models.ImageField(
                        default="default/default_avatar.png",
                        upload_to=user.models.photo_file_name,
                        verbose_name="Фото",
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(default=False, verbose_name="Адміністратор"),
                ),
                ("is_staff", models.BooleanField(default=False)),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="Активовано"),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Створено"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Оновлено"),
                ),
                (
                    "disliked_book",
                    models.ManyToManyField(
                        related_name="disliked_book",
                        to="forum.book",
                        verbose_name="Невподобані книги",
                    ),
                ),
                (
                    "disliked_discussion",
                    models.ManyToManyField(
                        related_name="disliked_discusion",
                        to="forum.discussion",
                        verbose_name="Невподобані обговорення",
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "liked_book",
                    models.ManyToManyField(
                        related_name="liked_book",
                        to="forum.book",
                        verbose_name="Вподобані книги",
                    ),
                ),
                (
                    "liked_discussion",
                    models.ManyToManyField(
                        related_name="liked_discusion",
                        to="forum.discussion",
                        verbose_name="Вподобані обговорення",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "Користувач",
                "verbose_name_plural": "Користувачі",
            },
        ),
    ]
