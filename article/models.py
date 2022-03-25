from django.db import models
from django.forms import CharField

class Usuario(models.Model):
    username = models.CharField(max_length=30)
    photo = models.ImageField()
    email = models.EmailField()
    password = models.CharField(max_length=30)
    USERNAME_FIELD = 'username'
    

class Commemt_second_level(models.Model):
    author_fk = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)

class Comment(models.Model):
    author_fk = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)
    comment_second_level = models.ForeignKey(Commemt_second_level, on_delete=models.CASCADE)

class Article(models.Model):
    title = models.CharField(max_length=1000)
    author_fk = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    text = CharField(max_length=100)
    image = models.ImageField()
    hearts = models.IntegerField()
    date = models.DateField()
    comments_fk = models.ForeignKey(Comment, on_delete=models.CASCADE)