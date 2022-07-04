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


@api_view(['GET'])
def feed_news(request):
    

    res = requests.get('https://feeds.npr.org/1004/feed.json')
    data = res.json()['items'][:5]

    for article_dict in data:
        add_data(article_dict)
        
        article = Article.objects.get(id=article_dict['id'])
        author = Author.objects.get(name=article_dict['author']['name'])

        if 'tags' in article_dict.keys():
            for tag in article_dict['tags']:
                tag_obj = Tag.objects.get(name=tag)
                article.tags.add(tag_obj)
            
        article.author = author
        article.save()

    return Response(data)


