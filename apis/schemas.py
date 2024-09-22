from calamus import fields
from calamus.schema import JsonLDSchema

from farm_management.models import (
    Farm,
)


ocsm_schema = fields.Namespace("http://w3id.org/ocsm/")



class NamedHistoricalBaseModelSchema(JsonLDSchema):
    id = fields.Id()
    name = fields.String(ocsm_schema.name)
    status = fields.Integer(ocsm_schema.status)
    created_at = fields.DateTime(ocsm_schema.createdAt)
    updated_at = fields.DateTime(ocsm_schema.updatedAt)
    deleted_at = fields.DateTime(ocsm_schema.deletedAt)



class FarmSchema(NamedHistoricalBaseModelSchema):
    class Meta:
        rdf_type = ocsm_schema.Farm
        model = Farm

