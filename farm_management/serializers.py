from rest_framework import serializers

from .models import FarmParcel, FarmPlant, FarmAnimal, FarmEquipment


class FarmParcelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FarmParcel

        fields = [
            'name', 'description', 'geo_id',
            'status', 'created_at', 'updated_at', 'deleted_at',
        ]


class FarmPlantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FarmPlant
        fields = [
            'name', 'description', 'area', 'geo_id',
            'species', 'variety',
            'status', 'created_at', 'updated_at', 'deleted_at',
        ]


class FarmAnimalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FarmAnimal
        fields = [
            'name', 'description','area', 'geo_id',
            'sex', 'castrated', 'species', 'breed', 'birth_date',
            'status', 'created_at', 'updated_at', 'deleted_at',
        ]


class FarmEquipmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FarmEquipment
        fields = [
            'name', 'description','area', 'geo_id',
            'purchase_date', 'manufacturer', 'model', 'seria_number',
            'status', 'created_at', 'updated_at', 'deleted_at',
        ]


