from rest_framework import serializers

from .models import Farm, FarmParcel, FarmCrop, FarmAnimal, AgriculturalMachine, Fertilizer


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


class FarmCropSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FarmCrop
        fields = [
            'name', 'description', 'parcel', 'geo_id',
            'species', 'variety',
            'status', 'created_at', 'updated_at', 'deleted_at',
        ]


class FarmAnimalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FarmAnimal
        fields = [
            'name', 'description','parcel', 'geo_id',
            'sex', 'castrated', 'species', 'breed', 'birth_date',
            'status', 'created_at', 'updated_at', 'deleted_at',
        ]


class AgriculturalMachineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AgriculturalMachine
        fields = [
            'name', 'description','parcel', 'geo_id',
            'purchase_date', 'manufacturer', 'model', 'seria_number',
            'status', 'created_at', 'updated_at', 'deleted_at',
        ]


class FertilizerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Fertilizer
        fields = [
            'name', 'description',
            'cost', 'price_unit', 'active_substance', 'targeted_towards',
            'nutrient_concentration',
            'status', 'created_at', 'updated_at', 'deleted_at',
        ]


