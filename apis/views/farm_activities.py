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
    CompostOperation,
    AddRawMaterialOperation,
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
    CompostOperationSerializer,
    AddRawMaterialOperationSerializer,
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

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.kwargs.get('compost_operation_pk'):
            queryset = queryset.filter(parent_activities=self.kwargs['compost_operation_pk'])
        return queryset


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



class CompostOperationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows CompostOperation to be viewed or edited.
    """
    queryset = CompostOperation.objects.all().prefetch_related('nested_activities').order_by('-start_datetime')
    serializer_class = CompostOperationSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['title','activity_type', 'compost_pile_id']


class AddRawMaterialOperationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows AddRawMaterialOperation to be viewed or edited.
    """
    queryset = AddRawMaterialOperation.objects.all().order_by('-start_datetime')
    serializer_class = AddRawMaterialOperationSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['title', 'activity_type']

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.kwargs.get('compost_operation_pk'):
            queryset = queryset.filter(parent_activities=self.kwargs['compost_operation_pk'])
        return queryset