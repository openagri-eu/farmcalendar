from django.db import models
from django.utils.translation import gettext_lazy as _

from simple_history.models import HistoricalRecords

from .base import BaseModel


class Farm(BaseModel):
    class Meta:
        verbose_name = "Farm"
        verbose_name_plural = "Farms"

    def __str__(self):
        return f"{self.name}"


class FarmParcel(BaseModel):
    class CultivationTypeChoices(models.TextChoices):
        GRAPES = 'grapes', _('Grapes')
        POTATO = 'potato', _('Potato')
        PASTURE = 'pasture', _('Pasture')

    farm = models.ForeignKey('Farm', on_delete=models.CASCADE, blank=False, null=False, related_name="farm_parcels")
    '''
    What do you think about this?
    related_name="%(class)ss" dynamically sets the related name using the model's class name. But it may not always 
    produce a meaningful or intuitive related name. Thus, I changed it to more descriptive and specific name.
    '''
    geo_id = models.UUIDField(_('Geographic Data ID'), unique=False, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    coordinates = models.CharField(max_length=255, default="0.0,0.0")  # Default as lat/lon format
    area = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)  # Area in hectares
    cultivation_type = models.CharField(max_length=50, choices=CultivationTypeChoices.choices,
                                        default=CultivationTypeChoices.GRAPES)

    # Adding historical tracking
    history = HistoricalRecords(table_name='farm_parcels_history', user_related_name='+')

    class Meta:
        db_table = "farm_parcels"
        verbose_name = "Farm Parcel"
        verbose_name_plural = "Farm Parcels"

    def __str__(self):
        return f"{self.name} ({self.cultivation_type})"
