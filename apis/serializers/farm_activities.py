from rest_framework import serializers

from farm_activities.models import (
    FarmCalendarActivityType,
    FarmCalendarActivity,
    FertilizationOperation,
    IrrigationOperation,
    CropProtectionOperation,
    Observation,
    CropStressIndicatorObservation,
    CropGrowthStageObservation,
)

from .base import JSONLDSerializer
from ..schemas import QuantityValueModel



class FarmCalendarActivitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FarmCalendarActivity

        fields = [
            'activity_type', 'title', 'details',
            'start_datetime', 'end_datetime',
        ]
        # 'status', 'created_at', 'updated_at', 'deleted_at',


class FarmCalendarActivityTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FarmCalendarActivityType

        fields = [
            'name', 'description',
            'background_color', 'border_color', 'text_color',
        ]


class FertilizationOperationSerializer(JSONLDSerializer):
    class Meta:
        model = FertilizationOperation

        fields = [
            'activity_type', 'title', 'details',
            'id',
            'start_datetime', 'end_datetime',
            'applied_amount', 'applied_amount_unit',
            'application_method',
            'fertilizer', 'operated_on'
        ]

    def to_representation(self, instance):
        instance.has_applied_amount = QuantityValueModel(instance.applied_amount, instance.applied_amount_unit)
        return super().to_representation(instance)


class IrrigationOperationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = IrrigationOperation
        fields = '__all__'


class CropProtectionOperationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CropProtectionOperation
        fields = '__all__'

class ObservationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Observation
        fields = '__all__'


class CropStressIndicatorObservationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CropStressIndicatorObservation
        fields = '__all__'


class CropGrowthStageObservationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CropGrowthStageObservation
        fields = '__all__'

