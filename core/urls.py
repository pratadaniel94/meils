from core.views import *
from django.conf.urls import include, url
urlpatterns =[
    url(r'^$', index, name="index"),
    url(r'^index', index),
    url(r'^cadastro' , cadastro)

]