# Generated by Django 4.1 on 2022-10-15 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_alter_book_category_alter_book_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='slug',
            field=models.SlugField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='discussion',
            name='slug',
            field=models.SlugField(primary_key=True, serialize=False),
        ),
    ]