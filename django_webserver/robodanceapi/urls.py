from django.urls import path, include
from rest_framework import routers
from .views import RobotViewSet, DanceOffViewSet

app_name = 'robodanceapi'

router = routers.DefaultRouter(trailing_slash=False)
router.register('robots', RobotViewSet)
router.register('danceoffs', DanceOffViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
