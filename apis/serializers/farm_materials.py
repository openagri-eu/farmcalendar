from rest_framework import serializers

from farm_management.models import Fertilizer




class FertilizerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Fertilizer
        fields = [
            'name', 'description',
            'cost', 'price_unit', 'active_substance', 'targeted_towards',
            'nutrient_concentration',
            'status', 'created_at', 'updated_at', 'deleted_at',
        ]

