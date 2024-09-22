from rest_framework import permissions, viewsets

from farm_management.models import (
    Farm,
    FarmParcel,
)
from ..serializers import (
    FarmSerializer,
    FarmParcelSerializer,
)

from farm_calendar.renderer import JSONLDRenderer

class FarmViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Farm to be viewed or edited.
    """
    queryset = Farm.objects.all().order_by('-created_at')
    serializer_class = FarmSerializer
    permission_classes = [permissions.IsAuthenticated]
    renderer_classes = [JSONLDRenderer, ]



class FarmParcelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows FarmParcel to be viewed or edited.
    """
    queryset = FarmParcel.objects.all().order_by('-created_at')
    serializer_class = FarmParcelSerializer
    permission_classes = [permissions.IsAuthenticated]



