from django.urls import path, include
from rest_framework import routers
from .views import RobotViewSet

app_name = 'robodanceapi'

router = routers.DefaultRouter(trailing_slash=False)
router.register('robots', RobotViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
