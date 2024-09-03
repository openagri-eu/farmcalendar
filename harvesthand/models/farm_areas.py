from django.db import models
from django.utils.translation import gettext_lazy as _

from .base import NamedHistoricalBaseModel


class FarmArea(NamedHistoricalBaseModel):
    geo_id = models.UUIDField(_('Georaphic Data ID'), unique=False, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Farm Area"
        verbose_name_plural = "Farm Areas"

    def __str__(self):
        return f"{self.name}"