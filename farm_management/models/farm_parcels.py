import re

from django.db import models
from django.utils.translation import gettext_lazy as _

from simple_history.models import HistoricalRecords

from .base import BaseModel, ActivePageManager
from .validators import *


class FarmMaster(BaseModel):
    name = models.CharField(max_length=255, unique=True, blank=False, null=False, default="Unnamed")
    description = models.TextField(blank=True, null=True)
    administrator = models.CharField(max_length=255, blank=True, null=True)
    contact_person_firstname = models.CharField(max_length=255, blank=True, null=True)
    contact_person_lastname = models.CharField(max_length=255, blank=True, null=True)
    telephone = models.CharField(max_length=20, blank=True, null=True)
    vat_id = models.CharField(max_length=50, blank=True, null=True)

    objects = models.Manager()
    active_objects = ActivePageManager()

    class Meta:
        db_table = "farm_master"
        verbose_name = "Farm"
        verbose_name_plural = "Farms"

    def __str__(self):
        return f"{self.name}"

    def clean(self):
        errors = {}

        # Validate fields with the name pattern
        fields_to_validate = {
            'name': self.name,
            'administrator': self.administrator,
            'contact_person_firstname': self.contact_person_firstname,
            'contact_person_lastname': self.contact_person_lastname
        }

        for field_name, value in fields_to_validate.items():
            if value:
                try:
                    validate_name_field(value)
                except ValidationError as e:
                    errors[field_name] = e.messages

        # Validate telephone
        if self.telephone:
            try:
                validate_phone_number(self.telephone)
            except ValidationError as e:
                errors['telephone'] = e.messages

        # Validate VAT ID
        if self.vat_id:
            try:
                validate_vat_id(self.vat_id)
            except ValidationError as e:
                errors['vat_id'] = e.messages

        # Raise ValidationError if any errors exist
        if errors:
            raise ValidationError(errors)


class FarmAddress(BaseModel):
    farm = models.OneToOneField(FarmMaster, on_delete=models.CASCADE, related_name="address")
    admin_unit_l1 = models.CharField(max_length=255, blank=True, null=True)
    admin_unit_l2 = models.CharField(max_length=255, blank=True, null=True)
    address_area = models.CharField(max_length=255, blank=True, null=True)
    municipality = models.CharField(max_length=255, blank=True, null=True)
    community = models.CharField(max_length=255, blank=True, null=True)
    locator_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = "farm_address"
        verbose_name = "Farm Address"
        verbose_name_plural = "Farm Addresses"

    def __str__(self):
        return f"Farm address for {self.farm.name}"

    def clean(self):
        if not self.admin_unit_l1:
            raise ValidationError("Admin Unit L1 is required.")
        if not self.municipality:
            raise ValidationError("Municipality is required.")


class FarmParcel(BaseModel):
    class CultivationTypeChoices(models.TextChoices):
        PASTURE = 'pasture', _('Pasture')
        ARABLE = 'arable', _('Arable')
        VINEYARD = 'vineyard', _('Vineyard')

    farm = models.ForeignKey('FarmMaster', on_delete=models.CASCADE, blank=False, null=False, related_name="farm_parcels")
    '''
    What do you think about this?
    related_name="%(class)ss" dynamically sets the related name using the model's class name. But it may not always 
    produce a meaningful or intuitive related name. Thus, I changed it to more descriptive and specific name.
    '''
    identifier = models.CharField(max_length=100, unique=True, blank=False, null=False, default="Unnamed")
    description = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=50, choices=CultivationTypeChoices.choices,
                                default=CultivationTypeChoices.ARABLE)
    valid_from = models.DateTimeField(blank=True, null=True)
    valid_to = models.DateTimeField(blank=True, null=True)
    in_region = models.CharField(max_length=255, blank=True, null=True)
    has_toponym = models.CharField(max_length=255, blank=True, null=True)
    area = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)  # Area in square meters
    is_nitro_area = models.BooleanField(default=False)
    is_natura2000_area = models.BooleanField(default=False)
    is_pdopg_area = models.BooleanField(default=False)
    is_irrigated = models.BooleanField(default=False)
    is_cultivated_in_levels = models.BooleanField(default=False)
    is_ground_slope = models.BooleanField(default=False)
    depiction = models.URLField(max_length=500, blank=True, null=True)
    # irrigation_system = models.ForeignKey(IrrigationSystem, on_delete=models.SET_NULL, null=True, blank=True, related_name="parcels")
    irrigation_flow = models.FloatField(blank=True, null=True)  # Flow rate in units???
    # crop = models.ForeignKey(Crop, on_delete=models.SET_NULL, null=True, blank=True, related_name="parcels")
    geo_id = models.UUIDField(_('Geographic Data ID'), unique=False, blank=True, null=True)
    coordinates = models.CharField(max_length=255, default="0.0,0.0")  # Default as lat/lon format

    class Meta:
        db_table = "farm_parcels"
        verbose_name = "Farm Parcel"
        verbose_name_plural = "Farm Parcels"

    def __str__(self):
        return f"{self.farm} ({self.category})"


# Model for Geometry
class FarmGeometry(BaseModel):
    farm_parcel = models.OneToOneField(FarmParcel, on_delete=models.CASCADE, related_name="geometry")
    geometry_type = models.CharField(max_length=50, default="Polygon")
    as_wkt = models.TextField()  # Well-Known Text representation of the geometry

    class Meta:
        db_table = "farm_geometry"
        verbose_name = "Farm Geometry"
        verbose_name_plural = "Farm Geometries"

    def __str__(self):
        return f"Farm Geometry for {self.farm_parcel.identifier}"


# Model for Location
class FarmLocation(BaseModel):
    farm_parcel = models.OneToOneField(FarmParcel, on_delete=models.CASCADE, related_name="location")
    latitude = models.FloatField()
    longitude = models.FloatField()

    class Meta:
        db_table = "farm_location"
        verbose_name = "Farm Location"
        verbose_name_plural = "Farm Locations"

    def __str__(self):
        return f"Farm Location for {self.farm_parcel.identifier}"


# Uncomment these models when ready to use irrigation and crop functionalities
#
# class IrrigationSystem(BaseModel):
#     name = models.CharField(max_length=255, blank=False, null=False)
#
#     class Meta:
#         verbose_name = "Irrigation System"
#         verbose_name_plural = "Irrigation Systems"
#
#     def __str__(self):
#         return self.name
#
#
# class CropSpecies(BaseModel):
#     name = models.CharField(max_length=255, blank=False, null=False)
#     alternate_name = models.CharField(max_length=255, blank=True, null=True)
#     agro_voc_concept = models.URLField(max_length=500, blank=True, null=True)
#
#     class Meta:
#         verbose_name = "Crop Species"
#         verbose_name_plural = "Crop Species"
#
#     def __str__(self):
#         return self.name
#
#
# class Crop(BaseModel):
#     name = models.CharField(max_length=255, blank=False, null=False)
#     species = models.ForeignKey(CropSpecies, on_delete=models.CASCADE, related_name="crops")
#     is_meant_for = models.CharField(max_length=255, blank=True, null=True)  # E.g., "table olives"
#
#     class Meta:
#         verbose_name = "Crop"
#         verbose_name_plural = "Crops"
#
#     def __str__(self):
#         return f"{self.name} ({self.species.name})"
