from django.urls import path
# from .views import  movies_list,movie_detail
from .views import MovieListAV, MovieDetails

urlpatterns = [
    # path('list/',movies_list,name='movies_list'),
    # path('list/<int:pk>/',movie_detail,name='movies_detail'),
    path('list/',MovieListAV.as_view()),
    path('list/<int:pk>',MovieDetails.as_view())
]