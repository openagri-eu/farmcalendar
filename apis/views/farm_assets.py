from rest_framework import permissions, viewsets

from farm_management.models import (
    GenericFarmAsset,
    FarmCrop,
    FarmAnimal,
    AgriculturalMachine,
)
from ..serializers import (
    GenericFarmAssetSerializer,
    FarmCropSerializer,
    FarmAnimalSerializer,
    AgriculturalMachineSerializer,
)



class GenericFarmAssetSerializerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows GenericFarmAsset to be viewed or edited.
    """
    queryset = GenericFarmAsset.objects.all().order_by('-created_at')
    serializer_class = GenericFarmAssetSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['name', 'parcel', 'status']


class FarmCropViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows FarmCrop to be viewed or edited.
    """
    queryset = FarmCrop.objects.all().order_by('-created_at')
    serializer_class = FarmCropSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['name', 'parcel', 'species', 'variety', 'growth_stage', 'status']


class FarmAnimalViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows FarmAnimal to be viewed or edited.
    """
    queryset = FarmAnimal.objects.all().order_by('-created_at')
    serializer_class = FarmAnimalSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['name', 'parcel', 'animal_group', 'status']


class AgriculturalMachineViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows AgriculturalMachine to be viewed or edited.
    """
    queryset = AgriculturalMachine.objects.all().order_by('-created_at')
    serializer_class = AgriculturalMachineSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['name', 'parcel', 'status']


