from django.shortcuts import render
from .models import Song

def song_list(request):
    songs_data = Song.objects.all().order_by('date')
    return render(request, 'songs/song_list.html', {'songs':songs_data})