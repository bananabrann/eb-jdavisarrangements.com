from django.urls import path
from . import views

urlpatterns = [
    # path('about/', views.about),
    path('', views.song_list)
]
