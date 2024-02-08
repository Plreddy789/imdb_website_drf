from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import MovieList
from .serializer import MovieSerializer


# Create your views here.

# def movies_list(request):
#     queryset = MovieList.objects.all()
#     data = {
#         'movies': list(queryset.values())
#     }
#     return JsonResponse(data)
#
#
# def movie_detail(request,pk):
#     queryset = MovieList.objects.get(pk=pk)
#     data={
#         'movie_name':queryset.movie_name,
#         'description':queryset.description,
#         'release_year':queryset.release_year,
#         'hero_name':queryset.hero_name,
#     }
#     return JsonResponse(data)

@api_view(['GET', 'POST'])
def movies_list(request):
    if request.method == 'GET':
        queryset = MovieList.objects.all()
        serializer = MovieSerializer(queryset, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error_messages,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail(request, pk):
    if request.method == 'GET':
        try:
            queryset = MovieList.objects.get(pk=pk)
        except MovieList.DoesNotExist:
            return Response({"message": "Movie not found"},status=status.HTTP_404_NOT_FOUND)
        serializer = MovieSerializer(queryset)
        return Response(serializer.data)
    if request.method == 'PUT':
        queryset = MovieList.objects.get(pk=pk)
        serializer = MovieSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data":serializer.data,"message":"successfully updated"},status=status.HTTP_202_ACCEPTED)
        else:
            return Response({"message":"enter all details"},status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        queryset = MovieList.objects.get(pk=pk)
        queryset.delete()
        return Response({'message': "Movie deleted successfully"},status=status.HTTP_204_NO_CONTENT)
