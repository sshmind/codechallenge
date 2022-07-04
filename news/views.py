from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests

from .serializers import AuthorSerializer, TagSerializer, ArticleSerializer
from .models import Author, Article, Tag



def add_data(some_dict):
    """serializer operations"""
    author_serializer = AuthorSerializer(data=some_dict['author'])
    if author_serializer.is_valid():
        author_serializer.save()
    
    if 'tags' in some_dict.keys():
        for tag in some_dict['tags']:
            tag_serializer = TagSerializer(data={'name': tag})
            if tag_serializer.is_valid():
                tag_serializer.save()
    


    article_serializer = ArticleSerializer(data=some_dict)
    if article_serializer.is_valid():
        article_serializer.save()


