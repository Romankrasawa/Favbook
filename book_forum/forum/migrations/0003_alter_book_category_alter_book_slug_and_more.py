# Generated by Django 4.1 on 2022-10-15 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.ManyToManyField(to='forum.category', verbose_name='Жанри'),
        ),
        migrations.AlterField(
            model_name='book',
            name='slug',
            field=models.SlugField(default='', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='discussion',
            name='slug',
            field=models.SlugField(default='', primary_key=True, serialize=False),
        ),
    ]