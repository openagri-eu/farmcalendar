from django.db import models
from django.utils.translation import gettext_lazy as _

from .base import NamedHistoricalBaseModel


class FarmArea(NamedHistoricalBaseModel):
    geo_id = models.UUIDField(_('Georaphic Data ID'), unique=False, blank=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Farm Area"
        verbose_name_plural = "Farm Areas"