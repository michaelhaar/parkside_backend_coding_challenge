from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .models import Robot
from .serializers import RobotSerializer


class RobotViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows robots to be viewed or edited.
    """
    queryset = Robot.objects.all().order_by('-id')
    serializer_class = RobotSerializer
    permission_classes = [permissions.AllowAny]
