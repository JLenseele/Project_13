from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('letting/', include('lettings.urls')),
    path('profile/', include('profiles.urls')),
    path('admin/', admin.site.urls),
]
