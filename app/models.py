from django.contrib.auth.models import User
from django.db import models


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    publish_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    author_name = models.CharField(max_length=100)
    profile_link = models.CharField('Ссылка на профиль', max_length=500)
    text = models.TextField()
