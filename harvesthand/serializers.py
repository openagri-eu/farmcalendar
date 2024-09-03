from rest_framework import serializers

from harvesthand.models import FarmPlant, FarmAnimal

class FarmPlantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FarmPlant
        fields = [
            'description','area', 'geo_id',
            'species', 'variety',
            'status', 'created_at', 'updated_at', 'deleted_at',
        ]


class FarmAnimalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FarmAnimal
        fields = [
            'description','area', 'geo_id',
            'sex', 'castrated', 'species', 'breed', 'birth_date',
            'status', 'created_at', 'updated_at', 'deleted_at',
        ]


