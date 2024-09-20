from rest_framework import permissions, viewsets

from farm_operations.models import FarmActivity, FarmActivityType
from farm_operations.serializers import FarmActivitySerializer, FarmActivityTypeSerializer


class FarmActivityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows FarmActivity to be viewed or edited.
    """
    queryset = FarmActivity.objects.all().order_by('-start_time')
    serializer_class = FarmActivitySerializer
    permission_classes = [permissions.IsAuthenticated]


class FarmActivityTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows FarmActivityType to be viewed or edited.
    """
    queryset = FarmActivityType.objects.all().order_by('-name')
    serializer_class = FarmActivityTypeSerializer
    permission_classes = [permissions.IsAuthenticated]

