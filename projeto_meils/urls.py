"""projeto_meils URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from core.views import *
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    url('admin/', admin.site.urls),
    url(r'^$', index, name="index"),
    url(r'^teste' , teste),
    url(r'^evento' , evento),
    url(r'^registrar' , registrar, name="registrar_usuario"),
    url(r'^registrado' , registrado, name="usuario_registrado"),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

