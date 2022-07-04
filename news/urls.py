from django.urls import path

from .views import feed_news, download_images


app_name = 'news'

urlpatterns = [
    path('feed_news/', feed_news, name='feed_news'),
    path('download_news_images/<int:count>/', download_images, name='download_image'),
]