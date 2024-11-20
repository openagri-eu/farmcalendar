from rest_framework import permissions, viewsets

from farm_activities.models import (
    FarmCalendarActivity,
    FarmCalendarActivityType,
    FertilizationOperation,
    IrrigationOperation,
    CropProtectionOperation,
    Observation,
    CropStressIndicatorObservation,
    CropGrowthStageObservation,
)
from ..serializers import (
    FarmCalendarActivitySerializer,
    FarmCalendarActivityTypeSerializer,
    FertilizationOperationSerializer,
    IrrigationOperationSerializer,
    CropProtectionOperationSerializer,
    ObservationSerializer,
    CropStressIndicatorObservationSerializer,
    CropGrowthStageObservationSerializer,
)


class FarmCalendarActivityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows FarmCalendarActivity to be viewed or edited.
    """
    queryset = FarmCalendarActivity.objects.all().order_by('-start_datetime')
    serializer_class = FarmCalendarActivitySerializer
    permission_classes = [permissions.IsAuthenticated]

    filterset_fields = ['title', 'activity_type', 'responsible_agent']


class FarmCalendarActivityTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows FarmCalendarActivityType to be viewed or edited.
    """
    queryset = FarmCalendarActivityType.objects.all().order_by('-name')
    serializer_class = FarmCalendarActivityTypeSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['name', ]


class FertilizationOperationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows FertilizationOperation to be viewed or edited.
    """
    queryset = FertilizationOperation.objects.all().order_by('-start_datetime')
    serializer_class = FertilizationOperationSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['title', 'activity_type', 'responsible_agent']


class IrrigationOperationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows IrrigationOperation to be viewed or edited.
    """
    queryset = IrrigationOperation.objects.all().order_by('-start_datetime')
    serializer_class = IrrigationOperationSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['title', 'activity_type', 'responsible_agent']


class CropProtectionOperationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows CropProtectionOperation to be viewed or edited.
    """
    queryset = CropProtectionOperation.objects.all().order_by('-start_datetime')
    serializer_class = CropProtectionOperationSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['title', 'activity_type', 'responsible_agent']


class ObservationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Observation to be viewed or edited.
    """
    queryset = Observation.objects.all().order_by('-start_datetime')
    serializer_class = ObservationSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['title','activity_type', 'responsible_agent']


class CropStressIndicatorObservationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows CropStressIndicator to be viewed or edited.
    """
    queryset = CropStressIndicatorObservation.objects.all().order_by('-start_datetime')
    serializer_class = CropStressIndicatorObservationSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['title','activity_type', 'responsible_agent']


class CropGrowthStageObservationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows CropGrowthStageObservation to be viewed or edited.
    """
    queryset = CropGrowthStageObservation.objects.all().order_by('-start_datetime')
    serializer_class = CropGrowthStageObservationSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['title','activity_type', 'responsible_agent']



