from rest_framework import permissions, viewsets
from farm_management.models import (
    Farm,
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
    queryset = Farm.objects.all().prefetch_related('farm_parcels').order_by('-created_at')
    serializer_class = FarmSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['name', 'status']


class FarmParcelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows FarmParcel to be viewed or edited.
    """
    queryset = FarmParcel.objects.all().prefetch_related('farmcrops').order_by('-created_at')
    serializer_class = FarmParcelSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['identifier', 'farm', 'parcel_type', 'geo_id', 'status']



