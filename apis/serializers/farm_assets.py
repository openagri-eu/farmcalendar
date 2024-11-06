from rest_framework import serializers

from farm_management.models import FarmCrop, FarmAnimal, AgriculturalMachine


class FarmCropSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FarmCrop
        fields = [
            'id', 'name', 'description',
            'parcel', 'geo_id',
            'species', 'variety',
            'growth_stage',
            'status', 'created_at', 'updated_at', 'deleted_at',
        ]


class FarmAnimalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FarmAnimal
        fields = [
            'id', 'name', 'description',
            'parcel', 'geo_id',
            'sex', 'castrated', 'species', 'breed', 'birth_date',
            'status', 'created_at', 'updated_at', 'deleted_at',
        ]


class AgriculturalMachineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AgriculturalMachine
        fields = [
            'id', 'name', 'description',
            'parcel', 'geo_id',
            'purchase_date', 'manufacturer', 'model', 'seria_number',
            'status', 'created_at', 'updated_at', 'deleted_at',
        ]


