"""bekia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import index, profile, about,safety,terms

from django.urls import path ,include
from django.conf import settings
from django.conf.urls.static import static
from .views import index, profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('profile/', profile , name='profile'),
    path('about/', about , name='about'),
    path('safety/', safety , name='safety'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('auth/', include('djoser.urls')),
    # path('auth/jwt', include('djoser.urls.jwt')),
    # path('auth/token', include('djoser.urls.authtoken')),
    path('terms/', terms , name='terms'),
    path('', include('accounts.urls')),
    path('', include('search.urls')),
    path('', include('contact.urls')),
    path('advertise/', include('advertise.urls')),
    # path('', include('search.urls')),
#     path('add_new_ad/', include('advertise.urls')),
]


if settings.DEBUG:
    urlpatterns=urlpatterns+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns=urlpatterns+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

