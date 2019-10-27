from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about),
    path('songs/', include('songs.urls')),
    path('', views.homepage)
]

urlpatterns += staticfiles_urlpatterns()