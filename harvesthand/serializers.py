from rest_framework import serializers

from harvesthand.models import FarmArea, FarmPlant, FarmAnimal


class FarmAreaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FarmArea

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


