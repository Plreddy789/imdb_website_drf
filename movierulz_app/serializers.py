from movierulz_app.models import VideosList, StreamPlatform, Reviews
from rest_framework import serializers

from rest_framework import serializers


class ReviewSerializer(serializers.ModelSerializer):
    # movie_name = serializers.SerializerMethodField()
    # reviewer_name = serializers.SerializerMethodField()

    class Meta:
        model = Reviews
        fields = '__all__'

    # def get_movie_name(self, reviews):
    #     return reviews.movie_name.movie_name
    #
    # def get_reviewer_name(self, reviews):
    #     return reviews.reviewer_name.username


class VideosListSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = VideosList
        fields = ['id', 'movie_name', 'description', 'release_year', 'hero_name', 'reviews']


class StreamPlatformSerializer(serializers.ModelSerializer):
    videoslist = VideosListSerializer(many=True, read_only=True)

    class Meta:
        model = StreamPlatform
        fields = '__all__'

# def get_len_movie_name(self, obj):
#     return len(obj.movie_name)
#
# def validate_movie_name(self, value):
#     if len(value) < 4:
#         raise serializers.ValidationError("name is too short enter the name above 2 characters")
#     else:
#         return value
#
# def validate(self, data):
#     if data['movie_name'] == data['description']:
#         raise serializers.ValidationError('name and description should be different')
#     else:
#         return data

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     movie_name = serializers.CharField()
#     description = serializers.CharField()
#     release_year = serializers.DateField()
#     hero_name = serializers.CharField()

# create method is used to create a new object in the database and this is used for POST requests
# def create(self, validated_data):
#     return MovieList.objects.create(**validated_data)

# update method is used to put method ,to change the whole record then we use this method
# def update(self, instance, validated_data):
#     instance.movie_name = validated_data.get('movie_name', instance.movie_name)
#     instance.description = validated_data.get('description', instance.description)
#     instance.release_year = validated_data.get('release_year', instance.release_year)
#     instance.hero_name = validated_data.get('hero_name', instance.hero_name)
#     instance.save()
#     return instance

# now field level validation
#     def validate_movie_name(self,value):
#         if len(value)<4:
#             raise serializers.ValidationError("name is too short enter the name above 2 characters")
#         else:
#             return value
#
# def validate(self,data):
#     if data['movie_name']==data['description']:
#         raise serializers.ValidationError('name and description should be different')
#     else:
#         return data
