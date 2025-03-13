from django.db import models
from django.contrib.auth.models import User

class Song(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)  # Track who uploaded
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    movie_name = models.CharField(max_length=200)
    audio_file = models.FileField(upload_to='songs/')
    cover_image = models.ImageField(upload_to='covers/', blank=True, null=True) 

    def __str__(self):
        return f"{self.title} - {self.artist} ({self.movie_name})"
