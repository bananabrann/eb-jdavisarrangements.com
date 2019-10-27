from django.shortcuts import render
from .models import Song

from django.http import HttpResponse

def song_list(request):
    songs_data = Song.objects.all().order_by('date')
    return render(request, 'songs/song_list.html', {'songs':songs_data})

def song_detail(request, slug):
    return HttpResponse(slug)