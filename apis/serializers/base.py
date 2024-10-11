from django.db.models.fields.related import ForeignKey, OneToOneField, ManyToManyField
from rest_framework import serializers

from ..schemas import OCSM_SCHEMA





class JSONLDSerializer(serializers.HyperlinkedModelSerializer):

    def _check_is_relationship_field(self, instance, field_name):
        # Get the model's meta information
        model = instance.__class__
        field = model._meta.get_field(field_name)

        return isinstance(field, (ForeignKey, OneToOneField, ManyToManyField))


    def _prepare_represetation(self, instance):
        json_dict_rep = super().to_representation(instance)
        base_rep = {}
        for field, value in json_dict_rep.items():
            correct_value = value
            if not self._check_is_relationship_field(instance, field):
                correct_value = getattr(instance, field)
            base_rep[field] = correct_value
        return base_rep

    def to_representation(self, instance):
        class_key = self.Meta.model.__name__
        ClassSchema = OCSM_SCHEMA[class_key]
        # representation = super().to_representation(instance)
        representation = self._prepare_represetation(instance)
        json_ld_representation = ClassSchema().dump(representation)

        return json_ld_representation