from rest_framework import permissions, viewsets

from farm_operations.models import FarmOperation, FarmOperationType
from farm_operations.serializers import FarmOperationSerializer, FarmOperationTypeSerializer


class FarmOperationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows FarmOperation to be viewed or edited.
    """
    queryset = FarmOperation.objects.all().order_by('-start_time')
    serializer_class = FarmOperationSerializer
    permission_classes = [permissions.IsAuthenticated]


class FarmOperationTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows FarmOperationType to be viewed or edited.
    """
    queryset = FarmOperationType.objects.all().order_by('-name')
    serializer_class = FarmOperationTypeSerializer
    permission_classes = [permissions.IsAuthenticated]

