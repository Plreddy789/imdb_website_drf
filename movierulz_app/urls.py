from django.urls import path
from .views import  movies_list,movie_detail

urlpatterns = [
    path('list/',movies_list,name='movies_list'),
    path('list/<int:pk>/',movie_detail,name='movies_detail'),

]