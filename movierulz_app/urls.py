from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# from .views import  movies_list,movie_detail
from .views import (VideosListAV, VideosListDetails,StreamPlatformVS
                    , ReviewsView, ReviewDetail,
                    ReviewCreate)

router=DefaultRouter()
router.register(r'stream', StreamPlatformVS,basename='stream platform')
urlpatterns = [
    path('api_auth',include('rest_framework.urls')),
    path('',include(router.urls)),

    # path('list/',movies_list,name='movies_list'),
    # path('list/<int:pk>/',movie_detail,name='movies_detail'),
    # path('stream/',StreamPlatformAV.as_view()),
    # path('stream/<int:pk>/',StreamPlatformDetails.as_view()),
    path('list/', VideosListAV.as_view()),
    path('list/<int:pk>', VideosListDetails.as_view()),
    path('stream/<int:pk>/reviews/',ReviewsView.as_view(),name='review_list'),
    path('stream/<int:pk>/review_create/',ReviewCreate.as_view()),
    path('stream/review/<int:pk>/',ReviewDetail.as_view(),name='review_detail'),

    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

