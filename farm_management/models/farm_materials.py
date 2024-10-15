from django.db import models
from django.utils.translation import gettext_lazy as _

from .base import NamedHistoricalBaseModel


class TreatmentMaterials(NamedHistoricalBaseModel):
    class Meta:
        # keep as abstract for now, maybe if we need to query
        # all assets in general, then it would make sense to have a
        # table for this model
        abstract = True

    description = models.TextField(blank=True, null=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    price_unit = models.CharField(max_length=255)
    active_substance = models.CharField(max_length=255)
    targeted_towards = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name} - {self.active_substance}'


class Fertilizer(TreatmentMaterials):
    class Meta:
        verbose_name = "Fertilizer"
        verbose_name_plural = "Fertilizers"

    nutrient_concentration = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f'{self.name} - {self.active_substance} - {self.nutrient_concentration}'
