from django.urls import path
from . import views

app_name = 'songs'

urlpatterns = [
    path('', views.song_list, name="list"),
    path('<slug>/', views.song_detail, name="detail")
]
