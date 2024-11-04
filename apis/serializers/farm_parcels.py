
from farm_management.models import Farm, FarmParcel
from .base import JSONLDSerializer


class FarmSerializer(JSONLDSerializer):
    class Meta:
        model = Farm

        fields = [
            'id', 'name',
            'status', 'created_at', 'updated_at', 'deleted_at',
        ]

    # def to_representation(self, instance):
    #     class_key = self.Meta.model.__name__
    #     ClassSchema = OCSM_SCHEMA[class_key]
    #     representation = super().to_representation(instance)
    #     json_ld_representation = ClassSchema().dump(representation)

    #     return json_ld_representation


class FarmParcelSerializer(JSONLDSerializer):
    class Meta:
        model = FarmParcel

        fields = [
            'id', 'name',
            'geo_id',
            'farm',
            'cultivation_type',
            'status', 'created_at', 'updated_at', 'deleted_at',
        ]



