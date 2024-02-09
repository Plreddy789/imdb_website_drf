from rest_framework import serializers

from movierulz_app.models import MovieList


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    movie_name = serializers.CharField()
    description = serializers.CharField()
    release_year = serializers.DateField()
    hero_name = serializers.CharField()

    def create(self, validated_data):
        return MovieList.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.movie_name = validated_data.get('movie_name', instance.movie_name)
        instance.description = validated_data.get('description', instance.description)
        instance.release_year = validated_data.get('release_year', instance.release_year)
        instance.hero_name = validated_data.get('hero_name', instance.hero_name)
        instance.save()
        return instance
