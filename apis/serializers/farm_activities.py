import uuid

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers

from farm_management.models import (
    Fertilizer,
    Pesticide,
    CompostMaterial,
    FarmParcel,
    FarmCrop,
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
    CompostOperation,
    AddRawMaterialOperation,
    AddRawMaterialCompostQuantity,
    CompostTurningOperation,
)

from .base import URNRelatedField, URNCharField
from ..schemas import generate_urn


def quantity_value_serializer_factory(unit_field, value_field):

    class GenericQuantityValueFieldSerializer(serializers.Serializer):
        unit = serializers.CharField(source=unit_field, allow_null=True, required=False)
        hasValue = serializers.CharField(source=value_field)


        def to_representation(self, instance):
            value = getattr(instance, value_field)
            unit = getattr(instance, unit_field)
            uuid_orig_str = "".join([
                str(getattr(instance, unit_field, '')),
                str(getattr(instance, value_field, ''),)
            ])
            hash_uuid = str(uuid.uuid5(uuid.NAMESPACE_DNS, uuid_orig_str))
            return {
                '@id': generate_urn('QuantityValue',obj_id=hash_uuid),
                '@type': 'QuantityValue',
                'unit': unit,
                'hasValue': value,
            }
    return GenericQuantityValueFieldSerializer


class FarmCalendarActivitySerializer(serializers.ModelSerializer):
    activityType = URNRelatedField(class_names=['FarmCalendarActivityType'], source='activity_type', queryset=FarmCalendarActivityType.objects.all())
    hasStartDatetime = serializers.DateTimeField(source='start_datetime')
    hasEndDatetime = serializers.DateTimeField(source='end_datetime', allow_null=True, required=False)

    responsibleAgent = serializers.CharField(source='responsible_agent', allow_null=True, required=False)

    usesAgriculturalMachinery = URNRelatedField(class_names=['AgriculturalMachine'], source='agricultural_machinery', many=True, queryset=AgriculturalMachine.objects.all())

    class Meta:
        model = FarmCalendarActivity
        fields = [
            'id',
            'activityType', 'title', 'details',
            'hasStartDatetime', 'hasEndDatetime',
            'responsibleAgent', 'usesAgriculturalMachinery'
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        json_ld_representation = {
            '@type': 'Operation',
            '@id': generate_urn(instance.__class__.__name__, obj_id=representation.pop('id')),
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
            '@type': 'FarmActivityType',
            '@id': generate_urn('FarmActivityType', obj_id=representation.pop('id')),
            **representation
        }

        return json_ld_representation


class AppliedAmmountFieldSerializer(serializers.Serializer):
    unit = serializers.CharField(source='applied_amount_unit')
    numericValue = serializers.DecimalField(source='applied_amount', max_digits=17, decimal_places=2)


    def to_representation(self, instance):
        uuid_orig_str = "".join([
            str(getattr(instance, 'applied_amount_unit', '')),
            str(getattr(instance, 'applied_amount', ''),)
        ])
        hash_uuid = str(uuid.uuid5(uuid.NAMESPACE_DNS, uuid_orig_str))
        return {
            '@id': generate_urn('QuantityValue',obj_id=hash_uuid),
            '@type': 'QuantityValue',
            'unit': instance.applied_amount_unit,
            'numericValue': instance.applied_amount,
        }

class GenericOperationSerializer(FarmCalendarActivitySerializer):
    hasAppliedAmount = AppliedAmmountFieldSerializer(source='*')

    operatedOn = URNRelatedField(
        class_names=['Parcel'],
        queryset=FarmParcel.objects.all(),
        source='operated_on'
    )

class FertilizationOperationSerializer(GenericOperationSerializer):
    usesFertilizer = URNRelatedField(
        class_names=['Fertilizer'],
        queryset=Fertilizer.objects.all(),
        source='fertilizer',
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
    operatedOn = URNRelatedField(
        class_names=['Parcel'],
        queryset=FarmParcel.objects.all(),
        source='operated_on',
        allow_null=True
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


    def create(self, validated_data):
        if self.context['view'].kwargs.get('compost_operation_pk'):
            validated_data['parent_activity'] = self.context['view'].kwargs.get('compost_operation_pk')

        return super().create(validated_data)


class CropProtectionOperationSerializer(GenericOperationSerializer):
    usesPesticide = URNRelatedField(
        class_names=['Pesticide'],
        queryset=Pesticide.objects.all(),
        source='pesticide',
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


class MadeBySensorFieldSerializer(serializers.Serializer):
    name = serializers.CharField(source='sensor_id', allow_null=True)

    def to_representation(self, instance):
        uuid_orig_str = getattr(instance, 'sensor_id', '')
        if uuid_orig_str is None or uuid_orig_str is '':
            return {}
        hash_uuid = str(uuid.uuid5(uuid.NAMESPACE_DNS, uuid_orig_str))
        return {
            '@id': generate_urn('Sensor',obj_id=hash_uuid),
            '@type': 'Sensor',
            'name': instance.sensor_id,
        }

class ObservationSerializer(FarmCalendarActivitySerializer):
    phenomenonTime = serializers.DateTimeField(source='start_datetime')
    observedProperty = serializers.CharField(source='observed_property')
    hasResult = quantity_value_serializer_factory('value_unit', 'value')(source='*')
    madeBySensor = MadeBySensorFieldSerializer(source='*', allow_null=True, required=False)

    class Meta:
        model = Observation
        fields = [
            'id',
            'activityType',
            'title', 'details',
            'phenomenonTime',
            'hasEndDatetime',
            'madeBySensor',
            # 'responsibleAgent', 'usesAgriculturalMachinery',
            'hasResult',
            'observedProperty',
        ]


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation.update({'@type': 'Observation'})
        json_ld_representation = representation

        return json_ld_representation


    def create(self, validated_data):
        if self.context['view'].kwargs.get('compost_operation_pk'):
            validated_data['parent_activity'] = CompostOperation.objects.get(pk=self.context['view'].kwargs.get('compost_operation_pk'))

        return super().create(validated_data)


class CropStressIndicatorObservationSerializer(ObservationSerializer):
    hasAgriCrop = URNRelatedField(
        class_names=['FarmCrop'],
        queryset=FarmCrop.objects.all(),
        source='crop'
    )
    class Meta:
        model = CropStressIndicatorObservation
        fields = [
            'id',
            'activityType', 'title', 'details',
            'phenomenonTime',
            'hasEndDatetime',
            'madeBySensor',
            # 'responsibleAgent', 'usesAgriculturalMachinery',
            'hasAgriCrop',
            'hasResult',
            'observedProperty',
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation.update({'@type': 'CropStressIndicatorObservation'})
        json_ld_representation = representation

        return json_ld_representation

class CropGrowthStageObservationSerializer(ObservationSerializer):
    hasAgriCrop = URNRelatedField(
        class_names=['FarmCrop'],
        queryset=FarmCrop.objects.all(),
        source='crop'
    )
    class Meta:
        model = CropGrowthStageObservation
        fields = [
            'id',
            'activityType', 'title', 'details',
            'phenomenonTime',
            'hasEndDatetime',
            'madeBySensor',
            # 'responsibleAgent', 'usesAgriculturalMachinery',
            'hasAgriCrop',
            'hasResult',
            'observedProperty',
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation.update({'@type': 'CropGrowthStageObservation'})
        json_ld_representation = representation

        return json_ld_representation



class AddRawMaterialCompostQuantitySerializer(serializers.ModelSerializer):
    quantityValue = AppliedAmmountFieldSerializer(source='*')
    typeName = serializers.CharField(source='material.name')

    class Meta:
        model = AddRawMaterialCompostQuantity
        fields = [
            'id',
            'typeName',
            'quantityValue',
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        json_ld_representation = {
            '@type': 'CompostMaterial',
            '@id': generate_urn('CompostMaterial', obj_id=representation.pop('id')),
            **representation
        }
        return json_ld_representation


class AddRawMaterialOperationSerializer(GenericOperationSerializer):
    hasCompostMaterial = AddRawMaterialCompostQuantitySerializer(source='addrawmaterialcompostquantity_set', many=True)

    class Meta:
        model = AddRawMaterialOperation

        fields = [
            'id',
            'activityType', 'title', 'details',
            'hasStartDatetime', 'hasEndDatetime',
            'responsibleAgent', 'usesAgriculturalMachinery',
            'hasCompostMaterial'
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation.update({'@type': 'AddRawMaterialOperation'})
        json_ld_representation = representation

        return json_ld_representation



    def create(self, validated_data):
        if self.context['view'].kwargs.get('compost_operation_pk'):
            validated_data['parent_activity'] = self.context['view'].kwargs.get('compost_operation_pk')

        compost_data = validated_data.pop('addrawmaterialcompostquantity_set', [])
        operation = super().create(validated_data)

        for compost in compost_data:
            material = CompostMaterial.objects.get_or_create(name=compost.pop('material')['name'])[0]
            AddRawMaterialCompostQuantity.objects.create(operation=operation, material=material, **compost)

        return operation

    def update(self, instance, validated_data):
        compost_data = validated_data.pop('addrawmaterialcompostquantity_set', [])
        instance = super().update(instance, validated_data)

        instance.addrawmaterialcompostquantity_set.all().delete()
        for compost in compost_data:
            material = CompostMaterial.objects.get_or_create(name=compost.pop('material')['name'])[0]

            AddRawMaterialCompostQuantity.objects.create(operation=instance, material=material, **compost)

        return instance


class CompostTurningOperationSerializer(GenericOperationSerializer):

    class Meta:
        model = CompostTurningOperation

        fields = [
            'id',
            'activityType', 'title', 'details',
            'hasStartDatetime', 'hasEndDatetime',
            'responsibleAgent', 'usesAgriculturalMachinery',
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation.update({'@type': 'CompostTurningOperation'})
        json_ld_representation = representation

        return json_ld_representation

    def create(self, validated_data):
        if self.context['view'].kwargs.get('compost_operation_pk'):
            validated_data['parent_activity'] = self.context['view'].kwargs.get('compost_operation_pk')

        return super().create(validated_data)


class CompostPileFieldSerializer(serializers.Serializer):
    # pile_id = serializers.CharField(source='compost_pile_id')

    def to_representation(self, instance):
        return {
            '@id': generate_urn('CompostPile',obj_id=instance),
            '@type': 'CompostPile',
        }
    def to_internal_value(self, data):
        return data['']


class CompostOperationSerializer(FarmCalendarActivitySerializer):
    AllOWED_NESTED_OPERATIONS = [
        settings.DEFAULT_CALENDAR_ACTIVITY_TYPES['irrigation']['name'],
        settings.DEFAULT_CALENDAR_ACTIVITY_TYPES['add_raw_material_operation']['name']
    ]

    hasNestedOperation = URNRelatedField(
        class_names=None, source='nested_activities', many=True,
        read_only=True
    )

    hasMeasurement = URNRelatedField(
        class_names=None, source='nested_activities', many=True,
        read_only=True
    )

    # isOperatedOn = serializers.CharField(source='compost_pile_id')
    # isOperatedOn = CompostPileFieldSerializer(source='compost_pile_id')
    isOperatedOn = URNCharField(
        class_names=['CompostPile'], source='compost_pile_id', read_only=False
    )
    class Meta:
        model = CompostOperation

        fields = [
            'id',
            'activityType', 'title', 'details',
            'hasStartDatetime', 'hasEndDatetime',
            'responsibleAgent', 'usesAgriculturalMachinery',
            'isOperatedOn',
            'hasNestedOperation', 'hasMeasurement'
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation.update({'@type': 'CompostOperation'})
        json_ld_representation = representation
        clean_nested_activities = []
        clean_nested_obs = []
        json_and_instances_list = zip(
            json_ld_representation['hasNestedOperation'],
            instance.nested_activities.all()
        )
        for json_activity, nested_activity in json_and_instances_list:
            class_name = 'Observation'
            for field in ['addrawmaterialoperation', 'irrigationoperation', 'compostturningoperation']:
                try:
                    class_name = getattr(nested_activity, field).__class__.__name__
                    break
                except ObjectDoesNotExist as e:
                    continue

            fixed_id = json_activity['@id'].format(class_name=class_name)
            fixed_type = json_activity['@type'].format(class_name=class_name)
            json_activity['@id'] = fixed_id
            json_activity['@type'] = fixed_type
            if class_name == 'Observation':
                clean_nested_obs.append(json_activity)
            else:
                clean_nested_activities.append(json_activity)

        json_ld_representation['hasNestedOperation'] = clean_nested_activities
        json_ld_representation['hasMeasurement'] = clean_nested_obs
        return json_ld_representation
