from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests

from .serializers import AuthorSerializer, TagSerializer, ArticleSerializer
from .models import Author, Article, Tag



def add_data(article):
    """serializer operations"""
    author_serializer = AuthorSerializer(data=article['author'])
    if author_serializer.is_valid():
        author_serializer.save()
    
    if 'tags' in article.keys():
        for tag in article['tags']:
            tag_serializer = TagSerializer(data={'name': tag})
            if tag_serializer.is_valid():
                tag_serializer.save()
    


    article_serializer = ArticleSerializer(data=article)
    if article_serializer.is_valid():
        article_serializer.save()


