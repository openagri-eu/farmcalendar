from django.db import models
from django.utils.translation import gettext_lazy as _

from .base import NamedHistoricalBaseModel


class FarmAsset(NamedHistoricalBaseModel):
    description = models.TextField(blank=True, null=True)

    geo_id = models.UUIDField(_('Geographic Data ID'), unique=False, blank=True)

    area = models.ForeignKey('FarmArea', on_delete=models.SET_NULL,blank=True, null=True, related_name="%(class)ss")


    class Meta:
        # keep as abstract for now, maybe if we need to query
        # all assets in general, then it would make sense to have a
        # table for this model
        abstract = True


class FarmPlant(FarmAsset):

    class Meta:
        verbose_name = "Farm Plant"
        verbose_name_plural = "Farm Plants"

    species = models.CharField(max_length=255)
    variety = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.species} - {self.variety}"


class FarmAnimal(FarmAsset):
    class Meta:
        verbose_name = "Farm Animal"
        verbose_name_plural = "Farm Animals"

    class SexChoices(models.IntegerChoices):
        NONE = 0, _('N/A')
        FEMALE = 1, _('Female')
        MALE = 2, _('Male')


    sex = models.IntegerField(choices=SexChoices, default=SexChoices.NONE)
    castrated = models.BooleanField(default=False)
    # probably add later parents m2m field to self

    species = models.CharField(max_length=255)
    breed = models.CharField(max_length=255, blank=True, null=True)
    birth_date = models.DateTimeField()

    def __str__(self):
        return f"{self.name} - {self.species} - {self.breed}"


class FarmEquipment(FarmAsset):
    class Meta:
        verbose_name = "Farm Equipment"
        verbose_name_plural = "Farm Equipments"

    purchase_date = models.DateField()
    manufacturer = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    seria_number = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name} - {self.manufacturer} - {self.model}'


class FarmSensor(FarmAsset):
    class Meta:
        verbose_name = "Farm Sensor"
        verbose_name_plural = "Farm Sensors"

    # not sure this should be here... gonna leave out for now
    # data_stream_uri = models.URLField()
    sensor_type = models.CharField()
    public = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} - {self.sensor_type}'

