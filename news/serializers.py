from rest_framework import serializers

from .models import Tag, Author, Article


class AuthorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Author
        fields = ('name', 'url',)


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('name',)


class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    tags = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Article
        fields = ('id', 'url', 'title', 'summary', 'image', 'date_published', 'date_modified', 'author', 'tags')