import uuid

from rest_framework import serializers

from farm_management.models import Farm, FarmParcel
from .base import JSONLDSerializer


def snake_to_camel_lower(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.capitalize() for x in components[1:])


class FarmSerializer(JSONLDSerializer):
    farm_parcels = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Farm
        fields = '__all__'
        # fields = [
        #     'id', 'name',
        #     'status', 'created_at', 'updated_at', 'deleted_at',
        # ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        json_ld_representation = {
            '@type': 'Farm'
        }

        specific_attrs_mapping = {
            'id': '@id',
            'vat_id': 'vatID',
            'telephone': 'telephone',
            'area': 'area',
            'farm_parcels': 'hasAgriParcel',
            'description': 'description',
            'name': 'name',
        }
        if representation['contact_person_firstname']:
            contact_person = {
                'firstname': representation.pop('contact_person_firstname', ''),
                'lastname': representation.pop('contact_person_lastname', ''),
                '@type': "Person"
            }
            contact_person['@id'] = str(uuid.uuid5(uuid.NAMESPACE_DNS, contact_person['firstname'] + contact_person['lastname']))
            json_ld_representation['contactPerson'] = contact_person

        if representation['admin_unit_l1'] and representation['admin_unit_l2']:
            address = {
                'admin_unit_l1': representation.pop('admin_unit_l1', ''),
                'admin_unit_l2': representation.pop('admin_unit_l2', ''),
                'address_area': representation.pop('address_area', ''),
                'municipality': representation.pop('municipality', ''),
                'address_area': representation.pop('address_area', ''),
                'community': representation.pop('community', ''),
                'locator_name': representation.pop('locator_name', ''),
            }
            pre_hash_str = "".join(address.values())
            if pre_hash_str != "":
                address['@id'] = str(uuid.uuid5(
                    uuid.NAMESPACE_DNS,
                    pre_hash_str
                ))
                address['@type'] = 'Address'
                json_ld_representation['address'] = address


        for attr, value in representation.items():
            clean_attr = specific_attrs_mapping.get(attr, None)
            if clean_attr is None:
                clean_attr = f'has{"".join(word.title() for word in attr.split("_"))}'

            json_ld_representation[clean_attr] = value

        return json_ld_representation


class FarmParcelSerializer(JSONLDSerializer):
    farmcrops = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = FarmParcel

        fields = '__all__'
        # fields = [
        #     'id', 'name',
        #     'geo_id',
        #     'farm',
        #     'cultivation_type',
        #     'status', 'created_at', 'updated_at', 'deleted_at',
        # ]

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