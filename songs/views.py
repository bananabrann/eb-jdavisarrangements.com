from django.shortcuts import render

from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Song
from .forms import DocumentForm


def song_list(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Song(docfile = request.FILES['docfile'])
            newdoc.save()

            return HttpResponseRedirect(reverse('song_list'))
    else:
        form = DocumentForm()
    
    songs_data = Song.objects.all().order_by('date')
    return render(request, 'songs/song_list.html', {'songs': songs_data, 'form': form})

def song_detail(request, slug):
    return HttpResponse(slug)
