from django.contrib import admin
from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
        model = Category
        list_display = ('title',)
        search_fields = ('title',)
        filter_horizontal = ()
@admin.register(Book_comment)
class Book_commentAdmin(admin.ModelAdmin):
        model = Book_comment
        list_display = ('id','user', 'book', 'content')
        list_editable = ('user', 'content')
        list_display_links = ('id',)
        search_fields = ('id',)
        filter_horizontal = ()

@admin.register(Discussion_comment)
class Discussion_commentAdmin(admin.ModelAdmin):
        model = Discussion_comment
        list_display = ('id','user','discussion', 'answer', 'content')
        list_editable = ('user', 'content', 'answer')
        list_display_links = ('id',)
        search_fields = ('id',)
        filter_horizontal = ()
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
        model = Book
        list_display = ('user', 'title', 'slug', 'description', 'author', 'cover', 'status', 'year', 'created_at', 'views')
        list_editable = ('user', 'title', 'description', 'status', 'cover', 'year', 'views')
        list_display_links = ('slug',)
        list_filter = ('user', 'author', 'status', 'year')
        search_fields = ('title',)
        ordering = ('created_at', 'views')
        filter_horizontal = ()

@admin.register(Discussion)
class DiscussionAdmin(admin.ModelAdmin):
        model = Discussion
        list_display = ('user', 'title', 'slug', 'description', 'book', 'status', 'created_at')
        list_display_links = ('slug',)
        list_editable = ('user', 'title', 'description', 'book', 'status')
        list_filter = ('user', 'book', 'status')
        search_fields = ('title',)
        ordering = ('created_at',)
        filter_horizontal = ()
