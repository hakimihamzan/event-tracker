from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'generator'
urlpatterns = [
    path('', views.generating, name='generating'),
    path('checkin', views.generatedDone, name='generatedDone'),
    path('out', views.generating2, name='out')

]
