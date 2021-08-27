from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('', views.display_movies, name='display_movies'),
    path('create_rating/', views.create_rating, name='create_rating'),
    path('logout/', views.logout_view, name='logout_view')

    #don't uncomment this block unless you want to inject data into DB
    #path('data_filler/', views.data_filler, name='data_filler')
]
