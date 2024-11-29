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
    farm_parcels = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Farm
        fields = [
            'status', 'deleted_at', 'created_at', 'updated_at',
            'id', 'name', 'description', 'administrator',
            'telephone', 'vatID', 'farm_parcels',
            'contactPerson', 'address'
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        json_ld_representation = representation
        json_ld_representation['@id'] = str(instance.id)  # Set @id using the model's id

        return json_ld_representation

    # def update(self, instance, validated_data):
    #     if address_data:
    #         # Update the address fields
    #         instance.admin_unit_l1 = address_data.get('admin_unit_l1', instance.admin_unit_l1)
    #         instance.admin_unit_l2 = address_data.get('admin_unit_l2', instance.admin_unit_l2)
    #         instance.address_area = address_data.get('address_area', instance.address_area)
    #         instance.municipality = address_data.get('municipality', instance.municipality)
    #         instance.community = address_data.get('community', instance.community)
    #         instance.locator_name = address_data.get('locator_name', instance.locator_name)

    #     # Handle the update for other fields as usual
    #     return super().update(instance, validated_data)

# class FarmSerializer(JSONLDSerializer):
#     farm_parcels = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

#     class Meta:
#         model = Farm
#         fields = '__all__'
#         # fields = [
#         #     'id', 'name',
#         #     'status', 'created_at', 'updated_at', 'deleted_at',
#         # ]

#     def to_representation(self, instance):
#         representation = super().to_representation(instance)
#         json_ld_representation = {
#             '@type': 'Farm'
#         }

#         specific_attrs_mapping = {
#             'id': '@id',
#             'vat_id': 'vatID',
#             'telephone': 'telephone',
#             'area': 'area',
#             'farm_parcels': 'hasAgriParcel',
#             'description': 'description',
#             'name': 'name',
#         }
#         if representation['contact_person_firstname']:
#             contact_person = {
#                 'firstname': representation.pop('contact_person_firstname', ''),
#                 'lastname': representation.pop('contact_person_lastname', ''),
#                 '@type': "Person"
#             }
#             contact_person['@id'] = str(uuid.uuid5(uuid.NAMESPACE_DNS, contact_person['firstname'] + contact_person['lastname']))
#             json_ld_representation['contactPerson'] = contact_person

#         if representation['admin_unit_l1'] and representation['admin_unit_l2']:
#             address = {
#                 'admin_unit_l1': representation.pop('admin_unit_l1', ''),
#                 'admin_unit_l2': representation.pop('admin_unit_l2', ''),
#                 'address_area': representation.pop('address_area', ''),
#                 'municipality': representation.pop('municipality', ''),
#                 'address_area': representation.pop('address_area', ''),
#                 'community': representation.pop('community', ''),
#                 'locator_name': representation.pop('locator_name', ''),
#             }
#             pre_hash_str = "".join(address.values())
#             if pre_hash_str != "":
#                 address['@id'] = str(uuid.uuid5(
#                     uuid.NAMESPACE_DNS,
#                     pre_hash_str
#                 ))
#                 address['@type'] = 'Address'
#                 json_ld_representation['address'] = address


#         for attr, value in representation.items():
#             clean_attr = specific_attrs_mapping.get(attr, None)
#             if clean_attr is None:
#                 clean_attr = f'has{"".join(word.title() for word in attr.split("_"))}'

#             json_ld_representation[clean_attr] = value

#         return json_ld_representation


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