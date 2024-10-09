from calamus import fields
from calamus.schema import JsonLDSchema

from farm_management.models import (
    Farm, FarmParcel
)

from farm_operations.models import (
    FarmOperation,
    FertilizationOperation
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




# class FarmOperation(models.Model):
#     operation_type = models.ForeignKey(FarmOperationType, on_delete=models.CASCADE)
#     title = models.CharField(max_length=200)
#     start_time = models.DateTimeField()
#     end_time = models.DateTimeField()
#     details = models.TextField(blank=True, null=True)

#     def __str__(self):
#         return f"{self.title} ({self.start_time.strftime('%Y-%m-%d %H:%M')})"


# class FertilizationOperation(FarmOperation):
#     # treated_area = models.IntegerField(blank=True, null=True)
#     # fertilization_type = models.CharField(max_length=255, blank=True, null=True)
#     applied_amount = models.DecimalField(max_digits=10, decimal_places=2)
#     applied_amount_unit = models.CharField(max_length=255)
#     application_method = models.CharField(max_length=255, blank=True, null=True)

#     operated_on = models.ForeignKey('farm_management.FarmParcel', on_delete=models.CASCADE)
#     fertilizer = models.ForeignKey('farm_management.Fertilizer', on_delete=models.SET_NULL, blank=True, null=True)
#     # TreatmentPlan
#     def save(self, *args, **kwargs):
#         self.operation_type, _ = FarmOperationType.objects.get_or_create(name=settings.DEFAULT_OPERATION_TYPES['fertilization']['name'])
#         super().save(*args, **kwargs)

class FarmOperationSchema(JsonLDSchema):
    id = fields.Id()
    # plan?

    operation_type = fields.IRI(ocsm_namespace.operationType)
    details = fields.String(ocsm_namespace.description)

    # title = models.CharField(max_length=200)
    # start_time = models.DateTimeField()
    # end_time = models.DateTimeField()
    # details = models.TextField(blank=True, null=True)

    class Meta:
        rdf_type = ocsm_namespace.FarmOperation
        model = FarmOperation

class FertilizationOperationSchema(FarmOperationSchema):


#     # treated_area = models.IntegerField(blank=True, null=True)
#     # fertilization_type = models.CharField(max_length=255, blank=True, null=True)
#     applied_amount = models.DecimalField(max_digits=10, decimal_places=2)
#     applied_amount_unit = models.CharField(max_length=255)
#     application_method = models.CharField(max_length=255, blank=True, null=True)

#     operated_on = models.ForeignKey('farm_management.FarmParcel', on_delete=models.CASCADE)
#     fertilizer = models.ForeignKey('farm_management.Fertilizer', on_delete=models.SET_NULL, blank=True, null=True)
#     # TreatmentPlan


OCSM_SCHEMA['Farm'] = FarmSchema
OCSM_SCHEMA['FarmParcel'] = FarmParcelSchema





