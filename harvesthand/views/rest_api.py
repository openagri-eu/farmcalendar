from rest_framework import permissions, viewsets

from harvesthand.models import FarmPlant, FarmAnimal
from harvesthand.serializers import FarmPlantSerializer, FarmAnimalSerializer


class FarmPlantViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows FarmPlant to be viewed or edited.
    """
    queryset = FarmPlant.objects.all().order_by('-created_at')
    serializer_class = FarmPlantSerializer
    permission_classes = [permissions.IsAuthenticated]


class FarmAnimalViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows FarmAnimal to be viewed or edited.
    """
    queryset = FarmAnimal.objects.all().order_by('-created_at')
    serializer_class = FarmAnimalSerializer
    permission_classes = [permissions.IsAuthenticated]

