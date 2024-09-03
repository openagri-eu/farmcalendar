from rest_framework import permissions, viewsets

from harvesthand.models import (
    FarmArea,
    FarmPlant,
    FarmAnimal,
    FarmEquipment,
)
from harvesthand.serializers import (
    FarmAreaSerializer,
    FarmPlantSerializer,
    FarmAnimalSerializer,
    FarmEquipmentSerializer,
)



class FarmAreaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows FarmPlant to be viewed or edited.
    """
    queryset = FarmArea.objects.all().order_by('-created_at')
    serializer_class = FarmAreaSerializer
    permission_classes = [permissions.IsAuthenticated]


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


class FarmEquipmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows FarmEquipment to be viewed or edited.
    """
    queryset = FarmEquipment.objects.all().order_by('-created_at')
    serializer_class = FarmEquipmentSerializer
    permission_classes = [permissions.IsAuthenticated]

