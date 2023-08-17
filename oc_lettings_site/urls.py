from django.contrib import admin
from django.urls import include
from . import views

from django.urls import path


def trigger_error():
    lenseele_julien_p13_sentry = 1
    lenseele_julien_p13_sentry += 'error'


urlpatterns = [
    path('', views.index, name='index'),
    path('letting/', include('lettings.urls')),
    path('profile/', include('profiles.urls')),
    path('admin/', admin.site.urls),
    path('sentry-debug/', trigger_error),
]
