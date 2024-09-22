from rest_framework import serializers

from ..schemas import OCSM_SCHEMA



class JSONLDSerializer(serializers.HyperlinkedModelSerializer):

    def to_representation(self, instance):
        class_key = self.Meta.model.__name__
        ClassSchema = OCSM_SCHEMA[class_key]
        representation = super().to_representation(instance)
        json_ld_representation = ClassSchema().dump(representation)

        return json_ld_representation