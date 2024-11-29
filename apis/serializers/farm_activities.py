import uuid

from rest_framework import serializers

from farm_management.models import (
    Fertilizer,
    Pesticide,
    FarmParcel,
    AgriculturalMachine
)

from farm_activities.models import (
    FarmCalendarActivityType,
    FarmCalendarActivity,
    FertilizationOperation,
    IrrigationOperation,
    CropProtectionOperation,Observation,
    CropStressIndicatorObservation,
    CropGrowthStageObservation,
)

from .base import JSONLDSerializer
from ..schemas import QuantityValueModel


class FarmCalendarActivitySerializer(serializers.ModelSerializer):
    activityType = serializers.PrimaryKeyRelatedField(source='activity_type', queryset=FarmCalendarActivityType.objects.all())
    hasStartDatetime = serializers.DateTimeField(source='start_datetime')
    hasEndDatetime = serializers.DateTimeField(source='end_datetime', allow_null=True)

    responsibleAgent = serializers.CharField(source='responsible_agent')

    usesAgriculturalMachinery = serializers.PrimaryKeyRelatedField(source='agricultural_machinery', many=True, queryset=AgriculturalMachine.objects.all())

    class Meta:
        model = FarmCalendarActivity

        fields = [
            'id',
            'activityType', 'title', 'details',
            'hasStartDatetime', 'hasEndDatetime',
            'responsibleAgent', 'usesAgriculturalMachinery'
        ]
        # 'status', 'created_at', 'updated_at', 'deleted_at',

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        json_ld_representation = {
            '@type': 'Operation',
            '@id': representation.pop('id'),
            **representation
        }

        return json_ld_representation


class FarmCalendarActivityTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmCalendarActivityType

        fields = [
            'id',
            'name', 'description',
            'background_color', 'border_color', 'text_color',
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        json_ld_representation = {
            '@type': 'FarmActivityType', #?
            '@id': representation.pop('id'),
            **representation
        }

        return json_ld_representation


class AppliedAmmountFieldSerializer(serializers.Serializer):
    unit = serializers.CharField(source='applied_amount_unit')
    numericValue = serializers.DecimalField(source='applied_amount', max_digits=17, decimal_places=14)


    def to_representation(self, instance):
        uuid_orig_str = "".join([
            getattr(instance, 'applied_amount_unit', ''),
            str(getattr(instance, 'applied_amount', ''),)
        ])
        hash_uuid = str(uuid.uuid5(uuid.NAMESPACE_DNS, uuid_orig_str))
        return {
            '@id': hash_uuid,
            '@type': 'QuantityValue',
            'unit': instance.applied_amount_unit,
            'numericValue': instance.applied_amount,
        }

class GenericOperationSerializer(FarmCalendarActivitySerializer):
    hasAppliedAmount = AppliedAmmountFieldSerializer(source='*')

    operatedOn = serializers.PrimaryKeyRelatedField(
        queryset=FarmParcel.objects.all(),
        source='operated_on'
    )

class FertilizationOperationSerializer(GenericOperationSerializer):
    usesFertilizer = serializers.PrimaryKeyRelatedField(
        queryset=Fertilizer.objects.all(),
        allow_null=True
    )
    hasApplicationMethod = serializers.CharField(source='application_method', allow_null=True)
    class Meta:
        model = FertilizationOperation

        fields = [
            'id',
            'activityType', 'title', 'details',
            'hasStartDatetime', 'hasEndDatetime',
            'responsibleAgent', 'usesAgriculturalMachinery',
            'hasAppliedAmount', 'hasApplicationMethod',
            'usesFertilizer', 'operatedOn'
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation.update({'@type': 'FertilizationOperation'})
        json_ld_representation = representation

        return json_ld_representation


class IrrigationOperationSerializer(GenericOperationSerializer):
    usesIrrigationSystem = serializers.ChoiceField(
        choices=IrrigationOperation.IrrigationSystemChoices.choices,
        source='irrigation_system'
    )

    class Meta:
        model = IrrigationOperation

        fields = [
            'id',
            'activityType', 'title', 'details',
            'hasStartDatetime', 'hasEndDatetime',
            'responsibleAgent', 'usesAgriculturalMachinery',
            'hasAppliedAmount',
            'usesIrrigationSystem', 'operatedOn'
        ]


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation.update({'@type': 'IrrigationOperation'})
        json_ld_representation = representation

        return json_ld_representation

class CropProtectionOperationSerializer(GenericOperationSerializer):
    usesPesticide = serializers.PrimaryKeyRelatedField(
        queryset=Pesticide.objects.all(),
        allow_null=True
    )
    class Meta:
        model = CropProtectionOperation
        fields = [
            'id',
            'activityType', 'title', 'details',
            'hasStartDatetime', 'hasEndDatetime',
            'responsibleAgent', 'usesAgriculturalMachinery',
            'hasAppliedAmount',
            'usesPesticide', 'operatedOn'
        ]


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation.update({'@type': 'CropProtectionOperation'})
        json_ld_representation = representation

        return json_ld_representation

class ObservationSerializer(FarmCalendarActivitySerializer):
    class Meta:
        model = Observation
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation.update({'@type': 'CropObservation'})
        json_ld_representation = representation

        return json_ld_representation

class CropStressIndicatorObservationSerializer(FarmCalendarActivitySerializer):
    class Meta:
        model = CropStressIndicatorObservation
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation.update({'@type': 'CropStressIndicatorObservation'})
        json_ld_representation = representation

        return json_ld_representation

class CropGrowthStageObservationSerializer(FarmCalendarActivitySerializer):
    class Meta:
        model = CropGrowthStageObservation
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation.update({'@type': 'CropGrowthStageObservation'})
        json_ld_representation = representation

        return json_ld_representation

