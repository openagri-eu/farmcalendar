import uuid

from rest_framework import serializers

from ..schemas import generate_urn
from .base import URNRelatedField

from farm_management.models import FarmCrop, FarmAnimal, AgriculturalMachine, FarmParcel


class BaseFarmAssetSerializer(serializers.ModelSerializer):
    parcel = URNRelatedField(
        class_names=['FarmParcel'],
        queryset=FarmParcel.objects.all(),
    )

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        json_ld_representation = {
            '@id': generate_urn(instance.__class__.__name__, obj_id=representation.pop('id')),
            **representation
        }

        return json_ld_representation

class CropSpeciesSerializerField(serializers.Serializer):
    name = serializers.CharField(source='species')
    variety = serializers.CharField()

    def to_representation(self, instance):
        uuid_orig_str = "".join([
            getattr(instance, 'species', ''),
            getattr(instance, 'variety', ''),
        ])
        hash_uuid = str(uuid.uuid5(uuid.NAMESPACE_DNS, uuid_orig_str))
        return {
            '@id': generate_urn('CropType', obj_id=hash_uuid),
            '@type': 'CropType',
            'name': instance.species,
            'variety': instance.variety,
        }



class FarmCropSerializer(BaseFarmAssetSerializer):

    cropSpecies = CropSpeciesSerializerField(source='*')

    class Meta:
        model = FarmCrop
        fields = [
            'status', 'deleted_at', 'created_at', 'updated_at',
            'id', 'name', 'description',
            'parcel', 'cropSpecies',
            'growth_stage',
            'status', 'created_at', 'updated_at', 'deleted_at',
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        json_ld_representation = {
            '@type': 'Crop',
            **representation
        }

        return json_ld_representation


class FarmAnimalSerializer(BaseFarmAssetSerializer):
    class Meta:
        model = FarmAnimal
        fields = [
            'id', 'national_id', 'name', 'description',
            'parcel',
            'sex', 'castrated', 'species', 'breed', 'birth_date', 'animal_group',
            'status', 'created_at', 'updated_at', 'deleted_at',
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        json_ld_representation = {
            '@type': 'Animal',
            **representation
        }

        return json_ld_representation


class AgriculturalMachineSerializer(BaseFarmAssetSerializer):
    class Meta:
        model = AgriculturalMachine
        fields = [
            'id', 'name', 'description',
            'parcel',
            'purchase_date', 'manufacturer', 'model', 'seria_number',
            'status', 'created_at', 'updated_at', 'deleted_at',
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        json_ld_representation = {
            '@type': 'AgriculturalMachine',
            **representation
        }

        return json_ld_representation