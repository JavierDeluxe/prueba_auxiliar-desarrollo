from django.db import models
from django.forms import CharField
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.CharField(max_length=300)

class Comment_second_level(models.Model):
    author_fk = models.OneToOneField(UserProfile,on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)

class Comment(models.Model):
    author_fk = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)
    comment_second_level = models.OneToOneField(Comment_second_level, on_delete=models.CASCADE)

class Article(models.Model):
    title = models.CharField(max_length=1000)
    author_fk = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    text = CharField(max_length=1000)
    image = models.ImageField()
    hearts = models.IntegerField()
    date = models.DateField()
    comments_fk = models.ForeignKey(Comment, on_delete=models.CASCADE,null=True)
    
    def __str__(self) -> str:
        return self.title,self.author_fk,self.text,self.image,self.hearts,self.date,self.comments_fk