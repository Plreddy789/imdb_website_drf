from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE


# Create your models here.

class StreamPlatform(models.Model):
    platform_name = models.CharField(max_length=15)
    url = models.URLField(default="www.movierulz.com")

    def __str__(self):
        return self.platform_name


class VideosList(models.Model):
    movie_name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    platform = models.ForeignKey(to=StreamPlatform, on_delete=CASCADE, related_name='videoslist')
    release_year = models.DateField()
    hero_name = models.CharField(max_length=25)

    def __str__(self):
        return self.movie_name


class Reviews(models.Model):
    reviewer_name = models.ForeignKey(to=User, on_delete=models.DO_NOTHING)
    movie_name = models.ForeignKey(to=VideosList, on_delete=CASCADE, related_name='reviews')
    review_desc = models.TextField(max_length=1000, null=True, blank=True)
    rating = models.FloatField()

    def __str__(self):
        return f"{self.reviewer_name} - {self.movie_name} - Rating: {self.rating}"
