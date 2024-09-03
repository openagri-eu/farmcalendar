from rest_framework import permissions, viewsets

from harvesthand.models import (
    FarmArea,
)
from harvesthand.serializers import (
    FarmAreaSerializer,
)



class FarmAreaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows FarmPlant to be viewed or edited.
    """
    queryset = FarmArea.objects.all().order_by('-created_at')
    serializer_class = FarmAreaSerializer
    permission_classes = [permissions.IsAuthenticated]

