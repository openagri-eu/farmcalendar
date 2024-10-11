from rest_framework import serializers

from farm_activities.models import FarmCalendarActivityType, FarmCalendarActivity, FertilizationOperation

from .base import JSONLDSerializer
from ..schemas import QuantityValueModel



class FarmCalendarActivitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FarmCalendarActivity

        fields = [
            'activity_type', 'title', 'details',
            'start_datetime', 'end_datetime',
        ]
        # 'status', 'created_at', 'updated_at', 'deleted_at',


class FarmCalendarActivityTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FarmCalendarActivityType

        fields = [
            'name', 'description',
            'background_color', 'border_color', 'text_color',
        ]


class FertilizationOperationSerializer(JSONLDSerializer):
    class Meta:
        model = FertilizationOperation

        fields = [
            'activity_type', 'title', 'details',
            'id',
            'start_datetime', 'end_datetime',
            'applied_amount', 'applied_amount_unit',
            'application_method',
            'fertilizer', 'operated_on'
        ]

    def to_representation(self, instance):
        instance.has_applied_amount = QuantityValueModel(instance.applied_amount, instance.applied_amount_unit)
        return super().to_representation(instance)

    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)

    #     return {
    #         "@context": [
    #             "https://w3id.org/ocsm/main-context.jsonld"  # or your custom context
    #         ],
    #         "@graph": [
    #             {
    #                 "@id": f"urn:openagri:fertilization:{instance.id}",
    #                 "@type": "FertilizationOperation",
    #                 "description": representation["details"],
    #                 "hasTimestamp": representation["start_time"],
    #                 "usesFertilizer": {
    #                     "@id": f"urn:openagri:fertilization:product:{instance.fertilizer.id}",
    #                     "@type": "Fertilizer",
    #                     "hasCommercialName": "Your Commercial Name Here"  # Update as needed
    #                 },
    #                 "hasAppliedAmount": {
    #                     "@id": f"urn:openagri:fertilization:amount:{instance.id}",
    #                     "@type": "QuantityValue",
    #                     "numericValue": float(representation['applied_amount']),
    #                     "unit": representation['applied_amount_unit']
    #                 },
    #                 "hasApplicationMethod": representation["application_method"],
    #                 "operationType": f"urn:openagri:operationType:{instance.operation_type.id}",  # Update as needed
    #                 "isOperatedOn": f"urn:openagri:parcel:{instance.operated_on.id}"  # Update as needed
    #             }
    #         ]
    #     }

    # def to_representation(self, instance):
    #     class_key = __class__.__name__
    #     class_schema_details = fertilization_operation_schema[class_key]
    #     represntation = {}
    #     representation = super().to_representation(instance)
    #     for property, prop_detail in class_schema_details['properties'].items():

    #     # Add JSON-LD prop_detailfic properties here
    #     representation["@id"] = f"urn:openagri:fertilization:{instance.id}"
    #     representation["@type"] = "FertilizationOperation"
    #     return representation