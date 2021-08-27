from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models_service import *
from .forms import *
# Create your views here.


# to remove all the data entries Ratings.objects.all().delete()
def data_filler(request):
    fill_movies_model()
    return HttpResponse('Successful!')


# handles users that rated movies, users didn't rate any movie and none users
def display_movies(request):
    watched = Ratings.objects.filter(username=request.user.id)
    if watched:
        movies = get_recommendations(watched)
        query_list = []
        for i in range(len(movies)):
            # and (username=request.user.id)
            query = Movies.objects.get(Series_Title=movies[i])
            query_list.append(query)
        movies = query_list
    else:
        movies = Movies.objects.all()
    context = {'movies': movies}

    return render(request, 'newsfeed/movielist_light.html', context)

@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('/')

@login_required(login_url='login')
def create_rating(request):
    form = CreateRatingForm(request.POST)
    if form.is_valid():
        new_form = form.save(commit=False)
        new_form.username = request.user
        new_form.save()
        #form.save()
        #form = CreateRatingForm()
        return redirect('display_movies')
    context = {'form': form}
    return render(request, 'newsfeed/create_rating.html', context)

def dummy(request):
    watched = Ratings.objects.filter(username=request.user.id)
    return HttpResponse(watched)