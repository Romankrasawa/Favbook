# Generated by Django 4.2.1 on 2023-07-08 13:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("forum", "0004_alter_book_category"),
        ("user", "0002_remove_user_token"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="disliked_discussion",
            field=models.ManyToManyField(
                related_name="disliked_discussion",
                to="forum.discussion",
                verbose_name="Невподобані обговорення",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="liked_discussion",
            field=models.ManyToManyField(
                related_name="liked_discussion",
                to="forum.discussion",
                verbose_name="Вподобані обговорення",
            ),
        ),
    ]