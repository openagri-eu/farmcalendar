from rest_framework import serializers

from farm_operations.models import FarmOperationType, FarmOperation, FertilizationOperation


class FarmOperationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FarmOperation

        fields = [
            'operation_type', 'title', 'details',
            'start_time', 'end_time',
        ]
        # 'status', 'created_at', 'updated_at', 'deleted_at',


class FarmOperationTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FarmOperationType

        fields = [
            'name', 'description',
            'background_color', 'border_color', 'text_color',
        ]



class FertilizationOperationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FertilizationOperation

        fields = [
            'operation_type', 'title', 'details',
            'start_time', 'end_time',
            'applied_amount', 'applied_amount_unit',
            'application_method',
            'fertilizer', 'operated_on'
        ]

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