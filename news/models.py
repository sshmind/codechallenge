from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    url = models.URLField(null=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    
    name = models.CharField(max_length=30, primary_key=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    class Meta:
        ordering = ('-date_published', '-date_modified')
    id = models.CharField(max_length=10, primary_key=True)
    url = models.URLField()
    title = models.CharField(max_length=150)
    summary = models.TextField()
    image = models.URLField(null=True)
    date_published = models.DateTimeField()
    date_modified = models.DateTimeField(null=True)
    author = models.ForeignKey(Author, related_name='articles', on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
