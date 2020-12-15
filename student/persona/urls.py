from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'participants', views.ParticipantViewSet)


app_name='persona'
urlpatterns = [
    path('', views.generateQr, name="generateQr"),
    path('check-in/', views.generating, name="generating"),
    path('--api/', include(router.urls)),
    path('--api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]
