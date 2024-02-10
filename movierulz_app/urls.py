from django.urls import path
# from .views import  movies_list,movie_detail
from .views import VideosListAV,VideosListDetails,StreamPlatformAV,StreamPlatformDetails

urlpatterns = [
    # path('list/',movies_list,name='movies_list'),
    # path('list/<int:pk>/',movie_detail,name='movies_detail'),
    path('list/',VideosListAV.as_view()),
    path('list/<int:pk>',VideosListDetails.as_view()),
    path('stream/',StreamPlatformAV.as_view()),
    path('stream/<int:pk>/',StreamPlatformDetails.as_view()),
]