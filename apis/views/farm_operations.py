from rest_framework import permissions, viewsets

from farm_operations.models import FarmOperation, FarmOperationType, FertilizationOperation
from ..serializers import FarmOperationSerializer, FarmOperationTypeSerializer, FertilizationOperationSerializer
# from apis.renderer import JSONLDRenderer


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


class FertilizationOperationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows FertilizationOperation to be viewed or edited.
    """
    queryset = FertilizationOperation.objects.all().order_by('-start_time')
    serializer_class = FertilizationOperationSerializer
    permission_classes = [permissions.IsAuthenticated]

    # renderer_classes = [JSONLDRenderer, ]

