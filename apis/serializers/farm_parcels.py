import uuid

from rest_framework import serializers

from farm_management.models import Farm, FarmParcel
from .base import JSONLDSerializer


def snake_to_camel_lower(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.capitalize() for x in components[1:])

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

    # status = serializers.ChoiceField(choices=Farm.BaseModelStatus.choices)
    # deleted_at = serializers.DateTimeField(required=False, allow_null=True)
    # created_at = serializers.DateTimeField(read_only=True)
    # updated_at = serializers.DateTimeField(read_only=True)
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

        json_ld_representation['@id'] = str(representation.pop('id'))
        json_ld_representation['@type'] = 'Farm'

        return json_ld_representation

class GeometrySerializerField(serializers.Serializer):
    asWKT = serializers.CharField(source='geometry')

    def to_representation(self, instance):

        return {
            '@id': instance.geo_id,
            '@type': 'Geometry',
            'asWKT': instance.geometry
        }

class LocationSerializerField(serializers.Serializer):
    lat = serializers.DecimalField(source='latitude', max_digits=17, decimal_places=14)
    long = serializers.DecimalField(source='longitude', max_digits=17, decimal_places=14)

    def to_representation(self, instance):
        return {
            '@id': instance.geo_id,
            '@type': 'Point',
            'lat': instance.latitude,
            'long': instance.longitude,
        }


class FarmParcelSerializer(serializers.ModelSerializer):
    validFrom = serializers.DateTimeField(source='valid_from')
    validTo = serializers.DateTimeField(source='valid_to')
    category = serializers.CharField(source='parcel_type')
    hasAgriCrop = serializers.PrimaryKeyRelatedField(source='farmcrops', many=True, read_only=True)

    hasIrrigationFlow = serializers.DecimalField(
        max_digits=15, decimal_places=2, source='irrigation_flow', allow_null=True
    )
    category = serializers.CharField(source='parcel_type')
    inRegion = serializers.CharField(source='in_region', allow_null=True)
    hasToponym = serializers.CharField(source='has_toponym', allow_null=True)
    isNitroArea = serializers.BooleanField(source='is_nitro_area')
    isNatura2000Area = serializers.BooleanField(source='is_natura2000_area')
    isPdopgArea = serializers.BooleanField(source='is_pdopg_area')
    isIrrigated = serializers.BooleanField(source='is_irrigated')
    isCultivatedInLevels = serializers.BooleanField(source='is_cultivated_in_levels')
    isGroundSlope = serializers.BooleanField(source='is_ground_slope')
    hasGeometry = GeometrySerializerField(source='*')
    location = LocationSerializerField(source='*')
        # location = {
        #     '@id': geo_id,
        #     '@type': 'Point',
        #     'lat': representation.pop('latitude', ''),
        #     'long': representation.pop('longitude', ''),
        # }
        # json_ld_representation['location'] = location
    class Meta:
        model = FarmParcel

        fields = [
            'status', 'deleted_at', 'created_at', 'updated_at',
            'id', 'identifier', 'description', 'validFrom', 'validTo', 'area',
            'hasIrrigationFlow', 'category', 'inRegion', 'hasToponym',
            'isNitroArea', 'isNatura2000Area', 'isPdopgArea', 'isIrrigated',
            'isCultivatedInLevels', 'isGroundSlope', 'depiction',
            'hasGeometry', 'location', 'hasAgriCrop'
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        json_ld_representation = {
            '@type': 'Parcel',
            '@id': representation.pop('id'),
            **representation
        }

        return json_ld_representation