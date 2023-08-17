from django.contrib import admin
from django.urls import include
from . import views

from django.urls import path


def trigger_error(request):
    lenseele_julien_p13_sentry = 'error'
    return int(lenseele_julien_p13_sentry)


urlpatterns = [
    path('', views.index, name='index'),
    path('letting/', include('lettings.urls')),
    path('profile/', include('profiles.urls')),
    path('admin/', admin.site.urls),
    path('sentry-debug/', trigger_error),
]
