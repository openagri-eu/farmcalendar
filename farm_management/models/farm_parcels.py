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
