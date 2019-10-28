from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    desc = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    audio = models.FileField(upload_to='media/')
    # add in thumbnail
    # add in song file

    def __str__(self):
        return self.title

    def snippet(self):
        return self.desc[:50] + ' ...'
