from django.contrib import admin
from django.urls import path, include
from . import views

from django.urls import path

def trigger_error(request):
    Lenseele_Julien_P13_Sentry = 1
    Lenseele_Julien_P13_Sentry += 'error'

urlpatterns = [
    path('', views.index, name='index'),
    path('letting/', include('lettings.urls')),
    path('profile/', include('profiles.urls')),
    path('admin/', admin.site.urls),
    path('sentry-debug/', trigger_error),
]
