import uuid

from rest_framework import serializers

from ..schemas import generate_urn
from .base import URNRelatedField

from farm_management.models import FarmCrop, FarmAnimal, AgriculturalMachine, FarmParcel


class BaseFarmAssetSerializer(serializers.ModelSerializer):
    Parcel = URNRelatedField(
        source='parcel',
        class_names=['FarmParcel'],
        queryset=FarmParcel.objects.all(),
    )
    dateCreated = serializers.DateTimeField(source='created_at')
    dateModified = serializers.DateTimeField(source='updated_at')
    invalidatedAtTime = serializers.DateTimeField(source='deleted_at')

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
        variety = (getattr(instance, 'variety', '') or '')
        uuid_orig_str = "".join([
            getattr(instance, 'species', ''),
            variety,
        ])
        hash_uuid = str(uuid.uuid5(uuid.NAMESPACE_DNS, uuid_orig_str))
        return {
            '@id': generate_urn('CropType', obj_id=hash_uuid),
            '@type': 'CropType',
            'name': getattr(instance, 'species', ''),
            'variety': getattr(instance, 'species', ''),
        }



class FarmCropSerializer(BaseFarmAssetSerializer):

    cropSpecies = CropSpeciesSerializerField(source='*')

    class Meta:
        model = FarmCrop
        fields = [
            'status', 'invalidatedAtTime', 'dateCreated', 'dateModified',
            'id', 'name', 'description',
            'Parcel', 'cropSpecies',
            'growth_stage',
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        json_ld_representation = {
            '@type': 'Crop',
            **representation
        }

        return json_ld_representation


class FarmAnimalSerializer(BaseFarmAssetSerializer):
    birthdate = serializers.DateTimeField(source='birth_date')
    AnimalGroup = serializers.CharField(source='animal_group')

    class Meta:
        model = FarmAnimal
        fields = [
            'id', 'national_id', 'name', 'description',
            'Parcel',
            'sex', 'castrated', 'species', 'breed', 'birthdate', 'AnimalGroup',
            'status', 'invalidatedAtTime', 'dateCreated', 'dateModified',
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
            'Parcel',
            'purchase_date', 'manufacturer', 'model', 'seria_number',
            'status', 'invalidatedAtTime', 'dateCreated', 'dateModified',
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        json_ld_representation = {
            '@type': 'AgriculturalMachine',
            **representation
        }

        return json_ld_representation