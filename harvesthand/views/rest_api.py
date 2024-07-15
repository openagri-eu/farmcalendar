from rest_framework import permissions, viewsets

from harvesthand.models import FarmPlant
from harvesthand.serializers import FarmPlantSerializer


class FarmPlantViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows FarmPlant to be viewed or edited.
    """
    queryset = FarmPlant.objects.all().order_by('-created_at')
    serializer_class = FarmPlantSerializer
    permission_classes = [permissions.IsAuthenticated]

