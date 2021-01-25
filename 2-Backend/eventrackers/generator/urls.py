from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'participants', views.ParticipantViewSet)

app_name = 'generator'
urlpatterns = [
    path('', views.generating, name='generating'),
    path('checkin', views.generatedDone, name='generatedDone'),
    path('out', views.generating2, name='out'),
    path('tot', views.get_more_tables, name='get_more_tables'),
    path('--api/', include(router.urls)),
    path('--api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
