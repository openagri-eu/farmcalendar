import uuid

from rest_framework import serializers

from farm_management.models import FarmCrop, FarmAnimal, AgriculturalMachine

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
            '@id': hash_uuid,
            '@type': 'CropType',
            'name': instance.species,
            'variety': instance.variety,
        }


class FarmCropSerializer(serializers.ModelSerializer):

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
            '@id': representation.pop('id'),
            **representation
        }

        return json_ld_representation


class FarmAnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmAnimal
        fields = [
            'id', 'name', 'description',
            'parcel',
            'sex', 'castrated', 'species', 'breed', 'birth_date',
            'status', 'created_at', 'updated_at', 'deleted_at',
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        json_ld_representation = {
            '@type': 'Animal',
            '@id': representation.pop('id'),
            **representation
        }

        return json_ld_representation


class AgriculturalMachineSerializer(serializers.HyperlinkedModelSerializer):
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
            '@id': representation.pop('id'),
            **representation
        }

        return json_ld_representation