# from django.http import JsonResponse
# from django.shortcuts import render
# from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework import status, mixins, generics, viewsets
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import VideosList, StreamPlatform, Reviews
from .serializers import VideosListSerializer, StreamPlatformSerializer, ReviewSerializer


# Create your views here.

# def movies_list(request):
#     queryset = VideoList.objects.all()
#     data = {
#         'movies': list(queryset.values())
#     }
#     return JsonResponse(data)
#
#
# def movie_detail(request,pk):
#     queryset = VideoList.objects.get(pk=pk)
#     data={
#         'movie_name':queryset.movie_name,
#         'description':queryset.description,
#         'release_year':queryset.release_year,
#         'hero_name':queryset.hero_name,
#     }
#     return JsonResponse(data)

# @api_view(['GET', 'POST'])
# def movies_list(request):
#     if request.method == 'GET':
#         queryset = VideoList.objects.all()
#         serializer = VideoListSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#     if request.method == 'POST':
#         serializer = VideoListSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.error_messages,status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_detail(request, pk):
#     if request.method == 'GET':
#         try:
#             queryset = VideoList.objects.get(pk=pk)
#         except VideoList.DoesNotExist:
#             return Response({"message": "Movie not found"},status=status.HTTP_404_NOT_FOUND)
#         serializer = VideoListSerializer(queryset)
#         return Response(serializer.data)
#     if request.method == 'PUT':
#         queryset = VideoList.objects.get(pk=pk)
#         serializer = VideoListSerializer(queryset, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"data":serializer.data,"message":"successfully updated"},status=status.HTTP_202_ACCEPTED)
#         else:
#             return Response({"message":"enter all details"},status=status.HTTP_400_BAD_REQUEST)
#
#     if request.method == "DELETE":
#         queryset = VideoList.objects.get(pk=pk)
#         queryset.delete()
#         return Response({'message': "Movie deleted successfully"},status=status.HTTP_204_NO_CONTENT)


# class StreamPlatformAV(APIView):
#     def get(self, request):
#         queryset = StreamPlatform.objects.all()
#         serializer = StreamPlatformSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = StreamPlatformSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"data": serializer.data, "message": "successfully created the data"},
#                             status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class StreamPlatformDetails(APIView):
#     def get(self, request, pk):
#         try:
#             queryset = StreamPlatform.objects.get(pk=pk)
#
#         except StreamPlatform.DoesNotExist:
#             return Response({"message": "streamplatform not found"}, status=status.HTTP_404_NOT_FOUND)
#         seriailzer = StreamPlatformSerializer(queryset)
#         return Response(seriailzer.data, status=status.HTTP_200_OK)
#
#     def put(self, request, pk):
#         queryset = StreamPlatform.objects.get(pk=pk)
#
#         serializer = StreamPlatformSerializer(queryset, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"data": serializer.data, "message": "successfully updated"}, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.error_messages)
#
#     def delete(self, request, pk):
#         queryset = StreamPlatform.objects.get(pk=pk)
#         queryset.delete()
#         return Response({"message": "successfully deleted"}, status=status.HTTP_204_NO_CONTENT)
#

class VideosListAV(APIView):
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    def get(self, request):
        queryset = VideosList.objects.all()
        serializer = VideosListSerializer(queryset, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = VideosListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data, "message": "successfully created the data"},
                            status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VideosListDetails(APIView):
    def get(self, request, pk):
        try:
            queryset = VideosList.objects.get(pk=pk)

        except VideosList.DoesNotExist:
            return Response({"message": "Movie not found"}, status=status.HTTP_404_NOT_FOUND)
        seriailzer = VideosListSerializer(queryset)
        return Response(seriailzer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        queryset = VideosList.objects.get(pk=pk)

        serializer = VideosListSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data, "message": "successfully updated"}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.error_messages)

    def delete(self, request, pk):
        queryset = VideosList.objects.get(pk=pk)
        queryset.delete()
        return Response({"message": "successfully deleted"}, status=status.HTTP_204_NO_CONTENT)


#
# class ReviewsView(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     queryset = Reviews.objects.all()
#     serializer_class = ReviewSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class ReviewDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
#                    generics.GenericAPIView):
#     queryset = Reviews.objects.all()
#     serializer_class = ReviewSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


class ReviewsView(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Retrieve the movie pk from the URL
        pk = self.kwargs.get('pk')

        # Filter reviews based on the provided movie pk
        queryset = Reviews.objects.filter(movie_name=pk)

        return queryset


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewSerializer
    permiassion_class=[IsAuthenticated]
    authentication_classes = [TokenAuthentication]


class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        serializer.save(reviewer_name=self.request.user)


# class StreamPlatformVS(viewsets.ViewSet):
#     queryset = StreamPlatform.objects.all()
#     serializer_class = StreamPlatformSerializer
#
#     def list(self, request):
#         queryset = StreamPlatform.objects.all()
#         serializer = StreamPlatformSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#     def retrieve(self, request, pk=None):
#         queryset = StreamPlatform.objects.all()
#         platform= get_object_or_404(queryset, pk=pk)
#         serializer = StreamPlatformSerializer(platform)
#         return Response(serializer.data)
#
#
#     def put(self, request, pk):
#         queryset = StreamPlatform.objects.get(pk=pk)
#
#         serializer = StreamPlatformSerializer(queryset, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"data": serializer.data, "message": "successfully updated"}, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.error_messages)
#
#     def delete(self, request, pk):
#         queryset = StreamPlatform.objects.get(pk=pk)
#         queryset.delete()
#         return Response({"message": "successfully deleted"}, status=status.HTTP_204_NO_CONTENT)
#


class StreamPlatformVS(viewsets.ModelViewSet):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
