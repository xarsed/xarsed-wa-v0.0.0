"""
URL configuration for xarsed_wa project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.views.generic import RedirectView
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import GenericSitemap
from documentation.models import Article


info_dict = {
    "queryset": Article.objects.all()
}
sitemaps = {"article": GenericSitemap(info_dict, priority=0.6)}

urlpatterns = [
    path("admin/", admin.site.urls),
    path("home/", include("home.urls")),
    path("process/", include("process.urls")),
    path("documentation/", include("documentation.urls")),
    path("", RedirectView.as_view(url="home/")),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="django.contrib.sitemaps.views.sitemap"),
]



