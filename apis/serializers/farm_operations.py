from rest_framework import serializers

from farm_operations.models import FarmOperationType, FarmOperation, FertilizationOperation



fertilization_operation_schema = {
    "FertilizationOperation": {
        "type": "object",
        "properties": {
            "operation_type": {
                "type": "string",
                "format": "uri"
            },
            "title": {
                "type": "string",
                "maxLength": 200
            },
            "details": {
                "type": "string",
                "nullable": True
            },
            "start_time": {
                "type": "string",
                "format": "date-time"
            },
            "end_time": {
                "type": "string",
                "format": "date-time"
            },
            "applied_amount": {
                "type": "string",
                "format": "decimal",
                "pattern": r"^-?\d{0,8}(?:\.\d{0,2})?$"
            },
            "applied_amount_unit": {
                "type": "string",
                "maxLength": 255
            },
            "application_method": {
                "type": "string",
                "nullable": True,
                "maxLength": 255
            },
            "fertilizer": {
                "type": "string",
                "format": "uri",
                "nullable": True
            },
            "operated_on": {
                "type": "string",
                "format": "uri"
            }
        },
        "required": [
            "applied_amount",
            "applied_amount_unit",
            "end_time",
            "operated_on",
            "operation_type",
            "start_time",
            "title"
        ]
    }
}


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

    def to_representation(self, instance):
        class_key = __class__.__name__
        class_schema_details = fertilization_operation_schema[class_key]
        represntation = {}
        representation = super().to_representation(instance)
        for property, prop_detail in class_schema_details['properties'].items():

        # Add JSON-LD prop_detailfic properties here
        representation["@id"] = f"urn:openagri:fertilization:{instance.id}"
        representation["@type"] = "FertilizationOperation"
        return representation