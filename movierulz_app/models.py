from django.db import models


# Create your models here.
class MovieList(models.Model):
    movie_name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    release_year=models.DateField()
    hero_name=models.CharField(max_length=25)

    def __str__(self):
        return self.movie_name
