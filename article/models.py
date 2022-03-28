from django.db import models
from django.forms import CharField
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.CharField(max_length=300)

class Article(models.Model):
    title = models.CharField(max_length=1000)
    author_fk = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)
    image = models.CharField(max_length=1000)
    date = models.DateField()
    hearts = models.IntegerField()

class Comment(models.Model):
    author_fk = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)
    publicacion_fk = models.ForeignKey(Article, on_delete=models.CASCADE)

class Comment_second_level(models.Model):
    author_fk = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)
    comentario_fk = models.ForeignKey(Comment, on_delete=models.CASCADE)

    
    