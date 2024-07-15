from rest_framework import serializers

from harvesthand.models import FarmPlant

class FarmPlantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FarmPlant
        fields = [
            'area', 'species', 'variety',
            'planting_date', 'harvesting_date',
            'quantity', 'unit',
            'status', 'created_at', 'updated_at', 'deleted_at',
        ]


