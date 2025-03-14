import uuid
from rest_framework import serializers

from farm_management.models import (
    Fertilizer,
    Pesticide
)


from ..schemas import generate_urn



class BaseTreatmentMaterialsSerializer(serializers.ModelSerializer):
    # hasCost = serializers.CharField(source='in_region', allow_null=True)

    hasCommercialName = serializers.CharField(source='name')
    hasActiveSubstance = serializers.CharField(source='active_substance')
    hasCost = serializers.DecimalField(
        max_digits=10, decimal_places=2, source='cost',
    )
    isPricePer = serializers.CharField(source='price_unit')
    isTargetedTowards = serializers.CharField(source='targeted_towards')
    dateCreated = serializers.DateTimeField(source='created_at', read_only=True)
    dateModified = serializers.DateTimeField(source='updated_at', read_only=True)
    invalidatedAtTime = serializers.DateTimeField(source='deleted_at', read_only=True)

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        json_ld_representation = {
            '@id': generate_urn(instance.__class__.__name__, obj_id=representation.pop('id')),
            **representation
        }

        return json_ld_representation


class FertilizerSerializer(BaseTreatmentMaterialsSerializer):
    hasNutrientConcentration = serializers.CharField(source='nutrient_concentration')

    class Meta:
        model = Fertilizer
        fields = [
            'id',
            'hasCommercialName', 'description',
            'hasCost', 'isPricePer', 'hasActiveSubstance', 'isTargetedTowards',
            'hasNutrientConcentration',
            'status',
            'dateCreated', 'dateModified', 'invalidatedAtTime',
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation.update({'@type': 'Fertilizer'})
        json_ld_representation = representation

        return json_ld_representation


class PesticideSerializer(BaseTreatmentMaterialsSerializer):
    hasPreharvestInterval = serializers.IntegerField(source='preharvest_interval')
    class Meta:
        model = Pesticide
        fields = [
            'id',
            'hasCommercialName', 'description',
            'hasCost', 'isPricePer', 'hasActiveSubstance', 'isTargetedTowards',
            'hasPreharvestInterval',
            'status',
            'dateCreated', 'dateModified', 'invalidatedAtTime',
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation.update({'@type': 'Pesticide'})
        json_ld_representation = representation

        return json_ld_representation
