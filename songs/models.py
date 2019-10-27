from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    desc = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    # add in thumbnail
    # add in song file