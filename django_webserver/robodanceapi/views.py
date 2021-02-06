from rest_framework import viewsets, permissions
from .models import Robot, DanceOff
from .serializers import RobotSerializer, DanceOffSerializer


class RobotViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows the user to list/create/receive/update/destroy 
    robots
    """
    queryset = Robot.objects.all().order_by('-id')
    serializer_class = RobotSerializer
    permission_classes = [permissions.AllowAny]


class DanceOffViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows the user to list/create/receive/update/destroy 
    danceoffs.
    """
    queryset = DanceOff.objects.all().order_by('-id')
    serializer_class = DanceOffSerializer
    # TODO use IsAuthenticatedOrReadOnly permission later
    permission_classes = [permissions.AllowAny]

    def get_serializer(self, *args, **kwargs):
        """
        Extends the parent's get_serializer() function and sets `many=true` 
        if data is a list of objects.
        """
        if isinstance(kwargs.get("data", {}), list):
            kwargs["many"] = True

        return super(DanceOffViewSet, self).get_serializer(*args, **kwargs)
