import uuid

from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from simple_history.models import HistoricalRecords


class BaseModel(models.Model):
    class BaseModelStatus(models.IntegerChoices):
        INACTIVE = 0, 'Inactive'
        ACTIVE = 1, 'Active'
        DELETED = 2, 'Deleted'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, db_index=True, editable=False, unique=True,
                          blank=False, null=False, verbose_name='ID')

    status = models.IntegerField(choices=BaseModelStatus.choices, default=BaseModelStatus.ACTIVE, verbose_name='Status')
    deleted_at = models.DateTimeField(null=True, blank=True, verbose_name='Deleted At')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated At')

    # Dynamically set the history table name based on the model name
    history = HistoricalRecords(inherit=True)

    class Meta:
        abstract = True

    def soft_delete(self):
        self.status = self.BaseModelStatus.DELETED
        self.deleted_at = timezone.now()
        self.save(update_fields=['status', 'deleted_at'])


class LocationBaseModel(models.Model):
    latitude = models.DecimalField(_('Latitude'), max_digits=17, decimal_places=14, blank=True, null=True)
    longitude = models.DecimalField(_('Longitude'), max_digits=17, decimal_places=14, blank=True, null=True)

    geometry = models.TextField(_('Geometry (WKT EPSG:4326)'), blank=True, null=True)
    geo_id = models.UUIDField(_('Geographic Data ID'), unique=True, blank=True, null=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self.geometry:
            # Generate UUID based on the geometry string
            self.geo_id = uuid.uuid5(uuid.NAMESPACE_DNS, self.geometry)
        elif not self.geometry:
            self.geo_id = None
        super().save(*args, **kwargs)

    @property
    def coordinates(self):
        if self.latitude is not None and self.longitude is not None:
            return f"{self.latitude}, {self.longitude}"
        return "0.0,0.0"


class ActivePageManager(models.Manager):
    def get_queryset(self):
        # Exclude records with status set to DELETED (status=2)
        return super().get_queryset().filter(status__lt=BaseModel.BaseModelStatus.DELETED)


class NamedHistoricalBaseModel(BaseModel):

    name = models.CharField(max_length=100)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name
