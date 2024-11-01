from django.db import models
from django.utils.translation import gettext_lazy as _

from .base import BaseModel, ActivePageManager
from .validators import *


class FarmMaster(BaseModel):
    name = models.CharField(max_length=255, unique=True, blank=False, null=False, default="Unnamed",
                            validators=[validate_name_field])
    description = models.TextField(blank=True, null=True)
    administrator = models.CharField(max_length=255, blank=True, null=True, validators=[validate_name_field])
    contact_person_firstname = models.CharField(max_length=255, blank=True, null=True, validators=[validate_name_field])
    contact_person_lastname = models.CharField(max_length=255, blank=True, null=True, validators=[validate_name_field])
    telephone = models.CharField(max_length=20, blank=True, null=True, validators=[validate_phone_number])
    vat_id = models.CharField(max_length=50, blank=True, null=True, validators=[validate_vat_id])

    objects = models.Manager()
    active_objects = ActivePageManager()

    class Meta:
        db_table = "farm_master"
        verbose_name = "Farm"
        verbose_name_plural = "Farms"

    def __str__(self):
        return f"{self.name}"


class FarmAddress(BaseModel):
    farm = models.OneToOneField(FarmMaster, on_delete=models.CASCADE, related_name="address")
    admin_unit_l1 = models.CharField(max_length=255, blank=True, null=True, validators=[validate_name_field])
    admin_unit_l2 = models.CharField(max_length=255, blank=True, null=True, validators=[validate_name_field])
    address_area = models.CharField(max_length=255, blank=True, null=True, validators=[validate_name_field])
    municipality = models.CharField(max_length=255, blank=True, null=True, validators=[validate_name_field])
    community = models.CharField(max_length=255, blank=True, null=True, validators=[validate_name_field])
    locator_name = models.CharField(max_length=255, blank=True, null=True, validators=[validate_name_field])

    objects = models.Manager()
    active_objects = ActivePageManager()

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

    farm = models.ForeignKey('FarmMaster', on_delete=models.CASCADE, blank=False, null=False,
                             related_name="farm_parcels")
    '''
    What do you think about this?
    related_name="%(class)ss" dynamically sets the related name using the model's class name. But it may not always
    produce a meaningful or intuitive related name. Thus, I changed it to more descriptive and specific name.
    '''
    identifier = models.CharField(max_length=100, unique=True, blank=False, null=False, default="Unnamed",
                                  validators=[validate_name_field])
    description = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=50, choices=CultivationTypeChoices.choices,
                                default=CultivationTypeChoices.ARABLE)
    valid_from = models.DateTimeField(blank=True, null=True, validators=[validate_datetime_format])
    valid_to = models.DateTimeField(blank=True, null=True, validators=[validate_datetime_format])
    in_region = models.CharField(max_length=255, blank=True, null=True, validators=[validate_name_field])
    has_toponym = models.CharField(max_length=255, blank=True, null=True, validators=[validate_name_field])
    area = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)
    is_nitro_area = models.BooleanField(default=False)
    is_natura2000_area = models.BooleanField(default=False)
    is_pdopg_area = models.BooleanField(default=False)
    is_irrigated = models.BooleanField(default=False)
    is_cultivated_in_levels = models.BooleanField(default=False)
    is_ground_slope = models.BooleanField(default=False)
    depiction = models.URLField(max_length=500, blank=True, null=True)
    # irrigation_system = models.ForeignKey(IrrigationSystem, on_delete=models.SET_NULL, null=True, blank=True, related_name="parcels")
    irrigation_flow = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, validators=[validate_positive])
    # crop = models.ForeignKey(Crop, on_delete=models.SET_NULL, null=True, blank=True, related_name="parcels")
    geo_id = models.UUIDField(_('Geographic Data ID'), unique=False, blank=True, null=True)
    coordinates = models.CharField(max_length=255, default="0.0,0.0", validators=[validate_coordinates])

    objects = models.Manager()
    active_objects = ActivePageManager()

    class Meta:
        db_table = "farm_parcels"
        verbose_name = "Farm Parcel"
        verbose_name_plural = "Farm Parcels"

    def __str__(self):
        return f"{self.farm} ({self.category})"


# Model for Geometry
class FarmGeometry(BaseModel):
    farm_parcel = models.OneToOneField(FarmParcel, on_delete=models.CASCADE, related_name="geometry")
    geometry_type = models.CharField(max_length=50, default="Polygon", validators=[validate_name_field])
    as_wkt = models.TextField()  # Well-Known Text representation of the geometry

    objects = models.Manager()
    active_objects = ActivePageManager()

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

    objects = models.Manager()
    active_objects = ActivePageManager()

    class Meta:
        db_table = "farm_location"
        verbose_name = "Farm Location"
        verbose_name_plural = "Farm Locations"

    def __str__(self):
        return f"Farm Location for {self.farm_parcel.identifier}"
