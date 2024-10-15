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

    farm = models.ForeignKey('Farm', on_delete=models.CASCADE, blank=False, null=False, related_name="%(class)ss")
    geo_id = models.UUIDField(_('Georaphic Data ID'), unique=False, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}"
