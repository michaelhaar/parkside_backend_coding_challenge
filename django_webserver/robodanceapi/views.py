from django.utils.decorators import method_decorator
from django.conf import settings
from rest_framework import viewsets, permissions
from drf_yasg.utils import swagger_auto_schema
from .models import Robot, DanceOff
from .serializers import RobotSerializer, DanceOffSerializer

PAGE_SIZE = settings.REST_FRAMEWORK.get('PAGE_SIZE')


@method_decorator(name='list', decorator=swagger_auto_schema(
    operation_summary="List the {} latest robot".format(PAGE_SIZE),
    operation_description="List the {} latest robot".format(PAGE_SIZE)
))
@method_decorator(name='create', decorator=swagger_auto_schema(
    operation_summary="Create a new robot",
    operation_description="Create a new robot",
))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(
    operation_summary="Get a specific robot",
    operation_description="Get a specific robot",
))
class RobotViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows the user to list/create/receive/update/destroy 
    robots
    """
    queryset = Robot.objects.all().order_by('-id')
    serializer_class = RobotSerializer
    permission_classes = [permissions.AllowAny]
    http_method_names = ['get', 'post']


DANCEOFF_CREATE_DESC = """
Create a new danceoff between two distinct robots.

The `opponents` array must contain two different robot ids. 
The `winner` must be one of the `opponent` ids.

Note: This method can also be used to create multiple danceoffs with a single
request. e.g.:
```json
[
{
    "winner": 3,
    "opponents": [2, 3]
},
{
    "winner": 3,
    "opponents": [1, 3]
},
{
    "winner": 2,
    "opponents": [1, 2]
}
]
```
"""


@method_decorator(name='list', decorator=swagger_auto_schema(
    operation_summary="List the {} latest danceoffs".format(PAGE_SIZE),
    operation_description="List the {} latest danceoffs".format(PAGE_SIZE)
))
@method_decorator(name='create', decorator=swagger_auto_schema(
    operation_summary="Create a new danceoffs",
    operation_description=DANCEOFF_CREATE_DESC,
))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(
    operation_summary="Get a specific danceoff",
    operation_description="Get a specific danceoff",
))
class DanceOffViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows the user to list/create/receive/update/destroy 
    danceoffs.
    """
    queryset = DanceOff.objects.all().order_by('-id')
    serializer_class = DanceOffSerializer
    # TODO use IsAuthenticatedOrReadOnly permission later
    permission_classes = [permissions.AllowAny]
    http_method_names = ['get', 'post']

    def get_serializer(self, *args, **kwargs):
        """
        Extends the parent's get_serializer() function and sets `many=true` 
        if data is a list of objects.
        """
        if isinstance(kwargs.get("data", {}), list):
            kwargs["many"] = True

        return super(DanceOffViewSet, self).get_serializer(*args, **kwargs)
