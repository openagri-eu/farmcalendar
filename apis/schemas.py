from calamus import fields
from calamus.schema import JsonLDSchema

from farm_management.models import (
    Farm, FarmParcel
)


ocsm_namespace = fields.Namespace("http://w3id.org/ocsm/")

OCSM_SCHEMA = {}


class NamedHistoricalBaseModelSchema(JsonLDSchema):
    id = fields.Id()
    name = fields.String(ocsm_namespace.name)
    status = fields.Integer(ocsm_namespace.status)
    # created_at = fields.DateTime(ocsm_namespace.createdAt)
    # updated_at = fields.DateTime(ocsm_namespace.updatedAt)
    # deleted_at = fields.DateTime(ocsm_namespace.deletedAt)
    created_at = fields.String(ocsm_namespace.createdAt)
    updated_at = fields.String(ocsm_namespace.updatedAt)
    deleted_at = fields.String(ocsm_namespace.deletedAt)


class FarmSchema(NamedHistoricalBaseModelSchema):
    class Meta:
        rdf_type = ocsm_namespace.Farm
        model = Farm


class FarmParcelSchema(NamedHistoricalBaseModelSchema):
    farm = fields.IRI(ocsm_namespace.Farm)
    geo_id = fields.IRI(ocsm_namespace.geoId)
    description = fields.String(ocsm_namespace.description)


    class Meta:
        rdf_type = ocsm_namespace.FarmParcel
        model = FarmParcel

OCSM_SCHEMA['Farm'] = FarmSchema
OCSM_SCHEMA['FarmParcel'] = FarmParcelSchema





