from django.forms import ModelForm

from newsfeed.models import Ratings


class CreateRatingForm(ModelForm):


    class Meta:
        model = Ratings
        fields = ['movie_name', 'rating']

