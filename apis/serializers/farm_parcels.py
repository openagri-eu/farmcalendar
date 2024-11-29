import uuid

from rest_framework import serializers

from farm_management.models import Farm, FarmParcel
from .base import JSONLDSerializer


def snake_to_camel_lower(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.capitalize() for x in components[1:])

# ContactPersonField: This handles the serialization of the contact person's data.
class ContactPersonField(serializers.Serializer):
    firstname = serializers.CharField(source='contact_person_firstname')
    lastname = serializers.CharField(source='contact_person_lastname')

    def to_representation(self, instance):
        # Construct the @id for the contact person
        contact_person_id = str(uuid.uuid5(uuid.NAMESPACE_DNS, instance.contact_person_firstname + instance.contact_person_lastname))
        return {
            'firstname': instance.contact_person_firstname,
            'lastname': instance.contact_person_lastname,
            '@id': contact_person_id,
            '@type': 'Person'
        }

    # def to_internal_value(self, data):
    #     # Generate the @id for contact person when receiving input data
    #     firstname = data.get('firstname', '')
    #     lastname = data.get('lastname', '')
    #     return {
    #         'firstname': firstname,
    #         'lastname': lastname,
    #     }


# AddressField: This handles the serialization of the address data.
class AddressField(serializers.Serializer):
    adminUnitL1 = serializers.CharField(source='admin_unit_l1')
    adminUnitL2 = serializers.CharField(source='admin_unit_l2')
    addressArea = serializers.CharField(source='address_area')
    municipality = serializers.CharField()
    community = serializers.CharField()
    locatorName = serializers.CharField(source='locator_name')

    def to_representation(self, instance):
        address_str = "".join([
            getattr(instance, 'admin_unit_l1', ''),
            getattr(instance, 'admin_unit_l2', ''),
            getattr(instance, 'address_area', ''),
            getattr(instance, 'municipality', ''),
            getattr(instance, 'community', ''),
            getattr(instance, 'locator_name', '')
        ])
        address_id = str(uuid.uuid5(uuid.NAMESPACE_DNS, address_str))
        return {
            '@id': address_id,   # Add the generated ID
            '@type': 'Address',   # Set the type for JSON-LD
            'adminUnitL1': getattr(instance, 'admin_unit_l1'),
            'adminUnitL2': getattr(instance, 'admin_unit_l2'),
            'addressArea': getattr(instance, 'address_area'),
            'municipality': getattr(instance, 'municipality'),
            'community': getattr(instance, 'community'),
            'locatorName': getattr(instance, 'locator_name')
        }

class FarmSerializer(serializers.ModelSerializer):
    contactPerson = ContactPersonField(source='*')
    address = AddressField(source='*')

    status = serializers.ChoiceField(choices=Farm.BaseModelStatus.choices)
    deleted_at = serializers.DateTimeField(required=False, allow_null=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    administrator = serializers.CharField()
    telephone = serializers.CharField()
    vatID = serializers.CharField(source='vat_id')
    hasAgriParcel = serializers.PrimaryKeyRelatedField(source='farm_parcels', many=True, read_only=True)

    class Meta:
        model = Farm
        fields = [
            'status', 'deleted_at', 'created_at', 'updated_at',
            'id', 'name', 'description', 'administrator',
            'telephone', 'vatID', 'hasAgriParcel',
            'contactPerson', 'address'
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        json_ld_representation = representation
        json_ld_representation['@id'] = str(instance.id)
        json_ld_representation['@type'] = 'Farm'

        return json_ld_representation

class FarmParcelSerializer(JSONLDSerializer):
    farmcrops = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = FarmParcel

        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        json_ld_representation = {
            '@type': 'Parcel'
        }

        specific_attrs_mapping = {
            'id': '@id',
            'identifier': 'identifier',
            'description': 'description',
            'valid_from': 'validFrom',
            'valid_to': 'validTo',
            'area': 'area',
            'irrigation_flow': 'hasIrrigationFlow',
            'farmcrops': 'hasAgriCrop',
            'parcel_type': 'category',
        }
        geo_id = representation.pop('geo_id', '')
        if representation['geometry']:
            geometry = {
                '@id': geo_id,
                'asWKT': representation.pop('geometry', ''),
            }
            geometry['@type'] = 'Geometry'
            json_ld_representation['hasGeometry'] = geometry

        location = {
            '@id': geo_id,
            '@type': 'Point',
            'lat': representation.pop('latitude', ''),
            'long': representation.pop('longitude', ''),
        }
        json_ld_representation['location'] = location


        for attr, value in representation.items():
            clean_attr = specific_attrs_mapping.get(attr, None)
            if clean_attr is None:
                clean_attr = attr
                clean_attr = snake_to_camel_lower(attr)

            json_ld_representation[clean_attr] = value

        return json_ld_representation