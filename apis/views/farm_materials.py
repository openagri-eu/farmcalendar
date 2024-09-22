from rest_framework import permissions, viewsets

from farm_management.models import (
    Fertilizer,
)
from ..serializers import (
    FertilizerSerializer
)


class FertilizerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Fertilizer to be viewed or edited.
    """
    queryset = Fertilizer.objects.all().order_by('-created_at')
    serializer_class = FertilizerSerializer
    permission_classes = [permissions.IsAuthenticated]

