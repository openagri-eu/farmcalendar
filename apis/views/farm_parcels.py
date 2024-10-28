from rest_framework import permissions, viewsets
from farm_management.models import (
    FarmMaster,
    FarmParcel,
)
from ..serializers import (
    FarmSerializer,
    FarmParcelSerializer,
)


class FarmViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Farm to be viewed or edited.
    """
    queryset = FarmMaster.objects.all().order_by('-created_at')
    serializer_class = FarmSerializer
    permission_classes = [permissions.IsAuthenticated]


class FarmParcelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows FarmParcel to be viewed or edited.
    """
    queryset = FarmParcel.objects.all().order_by('-created_at')
    serializer_class = FarmParcelSerializer
    permission_classes = [permissions.IsAuthenticated]



