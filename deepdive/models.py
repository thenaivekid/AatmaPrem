from email.policy import default
from email.quoprimime import quote
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class PostItem(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.CharField(max_length=256)
    completed = models.BooleanField(default=False)


class Post(models.Model):
    title = models.CharField(max_length=32)
    desc = models.CharField(max_length=1024)
    item = models.ManyToManyField(PostItem,blank=True,related_name='item')
    page = models.CharField(max_length=16)


# class Quotes(models.Model):
#     quote = models.CharField(max_length=128)
#     saidby = models.CharField(max_length=32)

#     def __str__(self):
#         return f"{self.quote} -{self.saidby}"



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

    
# # class Meditions(UserInputs):
# #     meditation =models.CharField(max_length=32)

# # class Exercises(UserInputs):
# #     exercise =models.CharField(max_length=32) 


# # class CharismaTips(UserInputs):
# #     tip =models.CharField(max_length=32) 

# # class LeadershipTips(UserInputs):
# #     leading_tip =models.CharField(max_length=32) 

# # class Comrades(UserInputs):
# #     name =models.CharField(max_length=32) 
# #     service= models.CharField(max_length=32) 

# # class ObservationStratedy(UserInputs):
# #     stratedy =models.CharField(max_length=128)

# #for love


# #for spinningwheels
# # class ThemesOfTheDay(models.Model):
# #     theme= models.CharField(max_length=32)

# # class SocialDare(models.Model):
# #     dare= models.CharField(max_length=32)

# # class CharacterTraits(models.Model):
# #     charactertrait= models.CharField(max_length=32)

# # class Emotions(models.Model):
# #     emotion= models.CharField(max_length=32)

# # class Visualizatoins(models.Model):
# #     visualization= models.CharField(max_length=32)

# #for activity