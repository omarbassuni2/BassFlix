import pandas as pd
from django.http import HttpResponse

from .models import Movies


def get_recommendations_helper(movie_name, user_rating, similarity_matrix):
    scores = similarity_matrix[movie_name] * (user_rating - 2.5)
    return scores


def get_recommendations(movie_name_list):
    similarity_matrix = pd.read_csv('E:\Software Developement\Django\BassFlix\\newsfeed\similarity_matrix.csv')
    similarity_matrix.set_index('title')
    movies = pd.DataFrame()
    for i in range(len(movie_name_list)):
        movies = movies.append(get_recommendations_helper(str(movie_name_list[i]), movie_name_list[i].rating, similarity_matrix))
    movies = movies.sum().sort_values(ascending=False).reset_index()
    movies.columns = ['title', 'ratings']
    movies_watched_len = len(movie_name_list)
    #to exculed already seen movies
    movies = movies.iloc[movies_watched_len:, :]
    id_nums = movies['title'].to_numpy()[:10]
    id_names = similarity_matrix.iloc[id_nums, 0].to_numpy()
    return id_names


def fill_movies_model():
    df = pd.read_csv('E:\Software Developement\Django\BassFlix\\newsfeed\dataset.csv')
    df = df.iloc[:, 1:]
    movies_list = []
    for row in range(len(df.index)):
        movies_list.append(
        Movies(
            Poster_Link=df.iloc[row, 0],
            Series_Title=df.iloc[row, 1],
            Released_Year=df.iloc[row, 2],
            Certificate=df.iloc[row, 3],
            Runtime=df.iloc[row, 4],
            Genre=df.iloc[row, 5],
            IMDB_Rating=df.iloc[row, 6],
            Overview=df.iloc[row, 7],
            Meta_score=df.iloc[row, 8],
            Director=df.iloc[row, 9],
            Star1=df.iloc[row, 10],
            Star2=df.iloc[row, 11],
            Star3=df.iloc[row, 12],
            Star4=df.iloc[row, 13],
            No_of_Votes=df.iloc[row, 14],
            Gross=df.iloc[row, 15],
            movieId=df.iloc[row, 16],
            tags=df.iloc[row, 17]
            )
        )
    Movies.objects.bulk_create(movies_list)
