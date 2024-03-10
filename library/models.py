from django.contrib.auth.models import AbstractUser
from django.db import models



class Genre(models.Model):
    genre = models.CharField(max_length=50)
    def __str__(self):
        return self.genre

class User(AbstractUser):
    favorite_genres = models.ManyToManyField(Genre)    
    
class Book(models.Model):
    title = models.CharField(max_length=200)
    authors = models.CharField(max_length=200)
    published_date = models.DateField(null=True, blank=True)
    isbn_13 = models.CharField(max_length=13, unique=True, null=True, blank=True)  # Or an appropriate field type
    page_count = models.IntegerField(null=True, blank=True)
    cover_link = models.URLField(null=True, blank=True)
    language = models.CharField(max_length=10)
    genre = models.CharField(max_length=50) 
