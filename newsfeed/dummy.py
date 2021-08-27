import pandas as pd


def get_recommendations(movie_name_list):
    similarity_matrix = pd.read_csv('E:\Software Developement\Django\BassFlix\\newsfeed\similarity_matrix.csv')

    movies = pd.DataFrame()
    for movie, rating in movie_name_list:
        movies = movies.append((similarity_matrix[movie] * (rating - 2.5)))
    movies = movies.sum().sort_values(ascending=False).reset_index()
    movies.columns = ['title', 'ratings']
    movies_watched_len = len(movie_name_list)
    # to exclude already seen movies
    movies = movies.iloc[movies_watched_len:, :]
    idd = movies['title'].to_numpy()[:10]
    idd = similarity_matrix.iloc[idd, 0].to_numpy()
    # to get the ids of the movies with respect to their rank in the csv file
    print(idd[1])
    return idd


user_watched_movies = [('300', 4),
                       ('3:10 to Yuma', 4)]

movies = get_recommendations(user_watched_movies)
#movies.astype(str)
print(type(movies[1]))