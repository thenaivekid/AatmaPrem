from email.policy import default
from email.quoprimime import quote
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class PostItem(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.CharField(max_length=256)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.content


class Post(models.Model):
    title = models.CharField(max_length=32)
    desc = models.CharField(max_length=1024)
    image = models.CharField(max_length=128,default='https://img.freepik.com/premium-vector/king-crown-esport-logo-design_177315-269.jpg')
    item = models.ManyToManyField(PostItem,blank=True,related_name='item')
    page = models.CharField(max_length=16)
    slug = models.SlugField(unique=True)


    def __str__(self):
        return self.title


class AnalyzingPeople(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    person = models.CharField(max_length=32)
    openness =models.IntegerField(default=0)
    conscientiousness =models.IntegerField(default=0)
    extroversion =models.IntegerField(default=0)
    agreeableness =models.IntegerField(default=0)
    neuroticism =models.IntegerField(default=0)
    values = models.CharField(max_length=256)
    passions = models.CharField(max_length=256)
    similarities = models.CharField(max_length=256)
    importance = models.CharField(max_length=256)
    darkside = models.CharField(max_length=256)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.person

    
class Journal(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    highlights = models.CharField(max_length=1024)
    lowlights = models.CharField(max_length=1024)
    emotions = models.CharField(max_length=1024)
    knowledge = models.CharField(max_length=1024)
    other = models.CharField(max_length=1024)
    rating = models.IntegerField()

    def __str__(self):
        return self.date


class ExternalLink(models.Model):
    title = models.CharField(max_length=64)
    link = models.CharField(max_length=128)

    def __str__(self):
        return self.title