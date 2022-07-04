from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests

from .serializers import AuthorSerializer, TagSerializer, ArticleSerializer
from .models import Author, Article, Tag
from .utils import retrieve_image



def add_data(article):
    """serializer operations"""

    if 'author' in article.keys():
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
        
        if 'author' in article_dict.keys():
            author = Author.objects.get(name=article_dict['author']['name'])
            article.author = author
            article.save()
        
        if 'tags' in article_dict.keys():
            for tag in article_dict['tags']:
                tag_obj = Tag.objects.get(name=tag)
                article.tags.add(tag_obj)
                article.save()


    return Response(data)



@api_view(['GET'])
def download_images(request, count):
    articles = Article.objects.all().order_by('-date_published', '-date_modified')[:count]
    for article in articles:
        if article.image:
            retrieve_image(article.image, article.id)
    
    return Response({'message': 'Done'})