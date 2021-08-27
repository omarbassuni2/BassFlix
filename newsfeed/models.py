from django.db import models
from django.forms import forms

from accounts.models import User


# Create your models here.
class Movies(models.Model):
    Poster_Link = models.CharField(max_length=255, null=True)
    #mark it as unique
    Series_Title = models.CharField(max_length=255, null=True)
    Released_Year = models.IntegerField(null=True)
    Certificate = models.CharField(max_length=255, null=True)
    Runtime = models.CharField(max_length=255, null=True)
    Genre = models.CharField(max_length=255, null=True)
    IMDB_Rating = models.CharField(max_length=255, null=True)
    Overview = models.CharField(max_length=255, null=True)
    Meta_score = models.CharField(max_length=255, null=True)
    Director = models.CharField(max_length=255, null=True)
    Star1 = models.CharField(max_length=255, null=True)
    Star2 = models.CharField(max_length=255, null=True)
    Star3 = models.CharField(max_length=255, null=True)
    Star4 = models.CharField(max_length=255, null=True)
    No_of_Votes = models.IntegerField(null=True)
    Gross = models.CharField(max_length=255, null=True)
    movieId = models.CharField(max_length=255, null=True)
    tags = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.Series_Title


class Ratings(models.Model):
    RATING_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    username = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    movie_name = models.ForeignKey(Movies, null=True, on_delete=models.SET_NULL)
    rating = models.IntegerField(null=True)

    def __str__(self):
        # returns the username of the object of the user
        return self.movie_name.Series_Title