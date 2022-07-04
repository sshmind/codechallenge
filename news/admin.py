from django.contrib import admin

from .models import Author, Tag, Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    
    list_display = ['title', 'author', 'date_published']
    list_filter = ('author', 'date_published', 'date_modified')
    search_fields = ('title', 'author__name')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):

    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):

    list_display = ('name', 'url')
    search_fields = ('name',)