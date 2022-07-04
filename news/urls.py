from django.urls import path

from .views import feed_news


app_name = 'news'

urlpatterns = [
    path('feed_news/', feed_news, name='feed_news'),
]