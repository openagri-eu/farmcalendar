from rest_framework import permissions, viewsets

from farmactivities.models import Activity, ActivityType
from farmactivities.serializers import ActivitySerializer, ActivityTypeSerializer


class ActivityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows FarmActivity to be viewed or edited.
    """
    queryset = Activity.objects.all().order_by('-start_time')
    serializer_class = ActivitySerializer
    permission_classes = [permissions.IsAuthenticated]


class ActivityTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows FarmActivityType to be viewed or edited.
    """
    queryset = ActivityType.objects.all().order_by('-name')
    serializer_class = ActivityTypeSerializer
    permission_classes = [permissions.IsAuthenticated]

