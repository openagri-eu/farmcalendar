from rest_framework import serializers

from farm_management.models import Farm, FarmParcel


class FarmSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Farm

        fields = [
            'name',
            'status', 'created_at', 'updated_at', 'deleted_at',
        ]


class FarmParcelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FarmParcel

        fields = [
            'farm',
            'name', 'description', 'geo_id',
            'status', 'created_at', 'updated_at', 'deleted_at',
        ]

        ]


