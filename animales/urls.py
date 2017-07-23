from django.conf.urls import url
from . import views

app_name = 'animales'

urlpatterns = [
    url(r'^animales/$', views.animales_vista, name='animales'),
    url(r'^$', views.index, name='index'),
]
