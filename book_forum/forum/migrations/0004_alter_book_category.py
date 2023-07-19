# Generated by Django 4.2.1 on 2023-07-08 13:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("forum", "0003_discussion_views"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="category",
            field=models.ManyToManyField(
                related_name="book_category", to="forum.category", verbose_name="Жанри"
            ),
        ),
    ]