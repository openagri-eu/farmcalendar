from rest_framework import permissions, viewsets

from farm_management.models import (
    FarmCrop,
    FarmAnimal,
    AgriculturalMachine,
)
from farm_management.serializers import (
    FarmCropSerializer,
    FarmAnimalSerializer,
    AgriculturalMachineSerializer,
)



class FarmCropViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows FarmCrop to be viewed or edited.
    """
    queryset = FarmCrop.objects.all().order_by('-created_at')
    serializer_class = FarmCropSerializer
    permission_classes = [permissions.IsAuthenticated]


class FarmAnimalViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows FarmAnimal to be viewed or edited.
    """
    queryset = FarmAnimal.objects.all().order_by('-created_at')
    serializer_class = FarmAnimalSerializer
    permission_classes = [permissions.IsAuthenticated]


class AgriculturalMachineViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows AgriculturalMachine to be viewed or edited.
    """
    queryset = AgriculturalMachine.objects.all().order_by('-created_at')
    serializer_class = AgriculturalMachineSerializer
    permission_classes = [permissions.IsAuthenticated]

