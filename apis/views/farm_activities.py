from rest_framework import permissions, viewsets

from farm_activities.models import FarmCalendarActivity, FarmCalendarActivityType, FertilizationOperation
from ..serializers import FarmCalendarActivitySerializer, FarmCalendarActivityTypeSerializer, FertilizationOperationSerializer


class FarmCalendarActivityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows FarmCalendarActivity to be viewed or edited.
    """
    queryset = FarmCalendarActivity.objects.all().order_by('-start_datetime')
    serializer_class = FarmCalendarActivitySerializer
    permission_classes = [permissions.IsAuthenticated]


class FarmCalendarActivityTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows FarmCalendarActivityType to be viewed or edited.
    """
    queryset = FarmCalendarActivityType.objects.all().order_by('-name')
    serializer_class = FarmCalendarActivityTypeSerializer
    permission_classes = [permissions.IsAuthenticated]


class FertilizationOperationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows FertilizationOperation to be viewed or edited.
    """
    queryset = FertilizationOperation.objects.all().order_by('-start_datetime')
    serializer_class = FertilizationOperationSerializer
    permission_classes = [permissions.IsAuthenticated]


