from calamus import fields
from calamus.schema import JsonLDSchema


from farm_management.models import (
    Farm, FarmParcel
)

from farm_activities.models import (
    FarmCalendarActivity,
    FertilizationOperation
)

from .others import QuantityValueSchema


ocsm_namespace = fields.Namespace("http://w3id.org/ocsm/")


URN_BASE_NAMESPACE = 'urn:farmcalendar'

def generate_urn_prefix(*class_names):
    urn_prefix = ':'.join([URN_BASE_NAMESPACE] + list(*class_names))
    return urn_prefix

def generate_urn(*class_names, obj_id):
    urn_prefix = generate_urn_prefix(class_names)
    return f'{urn_prefix}:{obj_id}'


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



class FarmCalendarActivitySchema(JsonLDSchema):
    id = fields.Id()

    activity_type = fields.IRI(ocsm_namespace.activityType)
    details = fields.String(ocsm_namespace.description)
    start_datetime = fields.DateTime(ocsm_namespace.hasStartDatetime)
    end_datetime = fields.DateTime(ocsm_namespace.hasEndDatetime)


    class Meta:
        rdf_type = ocsm_namespace.FarmCalendarActivity
        model = FarmCalendarActivity


class FertilizationOperationSchema(FarmCalendarActivitySchema):

    # plan?
    # responsible_agent = fields.IRI(ocsm_namespace.Agent)

    # agricultural_machinery = fields.IRI(ocsm_namespace.AgriculturalMachine, many=True)
    activity_type = fields.IRI(ocsm_namespace.operationType)
    application_method = fields.String(ocsm_namespace.hasApplicationMethod)

    operated_on = fields.IRI(ocsm_namespace.isOperatedOn)
    fertilizer = fields.IRI(ocsm_namespace.usesFertilizer)

    has_applied_amount = fields.Nested(ocsm_namespace.hasAppliedAmount, QuantityValueSchema, many=False)  # Nested QuantityValue




# OCSM_SCHEMA['Farm'] = FarmSchema
# OCSM_SCHEMA['FarmParcel'] = FarmParcelSchema
# OCSM_SCHEMA['FertilizationOperation'] = FertilizationOperationSchema


