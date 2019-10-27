from django.urls import path
from . import views

urlpatterns = [
    path('', views.song_list),
    path('<slug>/', views.song_detail)
]
