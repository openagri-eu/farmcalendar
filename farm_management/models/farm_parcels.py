from django.db import models
from django.utils.translation import gettext_lazy as _

from .base import NamedHistoricalBaseModel


class Farm(NamedHistoricalBaseModel):
    class Meta:
        verbose_name = "Farm"
        verbose_name_plural = "Farms"

    def __str__(self):
        return f"{self.name}"


class FarmParcel(NamedHistoricalBaseModel):
    class Meta:
        verbose_name = "Farm Parcel"
        verbose_name_plural = "Farm Parcels"

    class CultivationTypeChoices(models.TextChoices):
        GRAPES = 'grapes', _('Grapes')
        POTATO = 'potato', _('Potato')
        PASTURE = 'pasture', _('Pasture')

    farm = models.ForeignKey('Farm', on_delete=models.CASCADE, blank=False, null=False, related_name="%(class)ss")
    geo_id = models.UUIDField(_('Georaphic Data ID'), unique=False, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    coordinates = models.CharField(max_length=255)  # store in lat/lon format
    area = models.DecimalField(max_digits=10, decimal_places=2)  # Area in hectares
    cultivation_type = models.CharField(max_length=50, choices=CultivationTypeChoices.choices,
                                        default=CultivationTypeChoices.GRAPES)

    def __str__(self):
        return f"{self.name} ({self.cultivation_type})"


class Activity(models.Model):
    class ActivityTypeChoices(models.TextChoices):
        IRRIGATION = 'irrigation', _('Irrigation')
        PEST_MANAGEMENT = 'pest_management', _('Pest Management')
        HARVESTING = 'harvesting', _('Harvesting')
        SCOUTING = 'scouting', _('Scouting')

    parcel = models.ForeignKey(FarmParcel, on_delete=models.CASCADE, related_name="activities")
    date = models.DateField()
    activity_type = models.CharField(max_length=50, choices=ActivityTypeChoices.choices)
    description = models.TextField(blank=True, null=True)  # Additional details

    def __str__(self):
        return f"{self.activity_type} on {self.date} ({self.parcel})"


class Observation(models.Model):
    class ObservationTypeChoices(models.TextChoices):
        GROWTH_STAGE = 'growth_stage', _('Growth Stage')
        PEST_INFESTATION = 'pest_infestation', _('Pest Infestation')
        DISEASE_INFESTATION = 'disease_infestation', _('Disease Infestation')
        FRUITS_COUNTED = 'fruits_counted', _('Fruits Counted')
        CANOPY_DETECTED = 'canopy_detected', _('Canopy Detected')

    parcel = models.ForeignKey(FarmParcel, on_delete=models.CASCADE, related_name="observations")
    observation_date = models.DateField()
    observation_type = models.CharField(max_length=50, choices=ObservationTypeChoices.choices)
    value = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.observation_type} on {self.observation_date} for {self.parcel}"

