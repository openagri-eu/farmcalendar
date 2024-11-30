from uuid import UUID

from django.db.models.fields.related import ForeignKey, OneToOneField, ManyToManyField

from rest_framework.relations import PrimaryKeyRelatedField, PKOnlyObject
from rest_framework import serializers

from ..schemas import OCSM_SCHEMA, generate_urn_prefix



class URNRelatedField(PrimaryKeyRelatedField):
    """
    A custom DRF field for representing relations using URNs.
    """
    def __init__(self, class_names, **kwargs):
        """
        :param class_name: The class name added to the prefix for the URN, e.g., 'urn:myapp:farm'.
        :param kwargs: Additional arguments for PrimaryKeyRelatedField.
        """
        self.urn_prefix = generate_urn_prefix(class_names)
        super().__init__(**kwargs)

    def to_representation(self, value):
        """
        Converts the related object to a URN string.
        """

        if isinstance(value, PKOnlyObject):
            uuid_value = value.pk
        else:
            uuid_value = value.id
        return f"{self.urn_prefix}:{uuid_value}"

    def to_internal_value(self, data):
        """
        Converts a URN string into a model instance.
        """
        # Validate URN format
        if not isinstance(data, str) or not data.startswith(f"{self.urn_prefix}:"):
            raise serializers.ValidationError(f"Invalid URN format. Expected prefix '{self.urn_prefix}:'.")

        # Extract the ID from the URN
        raw_id = data.split(':')[-1]

        # Ensure the ID is valid (UUID or integer depending on the target field)
        try:
            raw_id = UUID(raw_id)
        except (ValueError, TypeError):
            raise serializers.ValidationError("Invalid ID in URN.")

        # Fetch the related instance
        return super().to_internal_value(raw_id)


class JSONLDSerializer(serializers.ModelSerializer):

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
        try:
            ClassSchema = OCSM_SCHEMA[class_key]
        except KeyError:
            return super().to_representation(instance)
        representation = self._prepare_represetation(instance)
        json_ld_representation = ClassSchema().dump(representation)
        return json_ld_representation