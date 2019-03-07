"""CatDictionary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from center.views import CatListView, ImageListView, CatCreateView, ImageCreateView, CatImageCreateFormSetView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ImageListView.as_view(), name = "index"),
    path('create', CatCreateView.as_view(), name = "create"),
    path('images/upload', ImageCreateView.as_view(), name = "upload"),
    path('cats', CatListView.as_view(), name="cats"),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
