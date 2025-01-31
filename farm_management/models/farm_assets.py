from django.db import models
from django.utils.translation import gettext_lazy as _

from .base import NamedHistoricalBaseModel, BaseModel
from .validators import validate_comma_separated_float_list


class FarmAsset(NamedHistoricalBaseModel):
    class Meta:
        # keep as abstract for now, maybe if we need to query
        # all assets in general, then it would make sense to have a
        # table for this model
        abstract = True

    description = models.TextField(blank=True, null=True)
    parcel = models.ForeignKey('FarmParcel', on_delete=models.SET_NULL,blank=True, null=True,
                               related_name="%(class)ss")



class FarmCrop(FarmAsset):
    class Meta:
        verbose_name = "Farm Crop"
        verbose_name_plural = "Farm Crops"

    species = models.CharField(max_length=255)
    variety = models.CharField(max_length=255, blank=True, null=True)

    growth_stage = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.species} - {self.variety} - {self.growth_stage}"


class FarmAnimal(FarmAsset):
    class Meta:
        verbose_name = "Farm Animal"
        verbose_name_plural = "Farm Animals"

    class SexChoices(models.IntegerChoices):
        NONE = 0, _('N/A')
        FEMALE = 1, _('Female')
        MALE = 2, _('Male')

    name = models.CharField(_('Name'), max_length=100, blank=True, null=True)
    national_id = models.CharField(_('National ID'), blank=True, null=True)
    species = models.CharField(max_length=255)
    breed = models.CharField(max_length=255, blank=True, null=True)
    birth_date = models.DateTimeField()
    sex = models.IntegerField(choices=SexChoices.choices, default=SexChoices.NONE)
    castrated = models.BooleanField(default=False)
    animal_group = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        s = f"{self.species} - {self.breed}"
        if self.animal_group:
            s += f' ({self.animal_group})'
        return s


class AgriculturalMachine(FarmAsset):
    class Meta:
        verbose_name = "Farm Machine"
        verbose_name_plural = "Farm Machines"

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


class CompostPile(FarmAsset):
    class Meta:
        verbose_name = "Compost Pile"
        verbose_name_plural = "Compost Piles"

    class CompostingStageChoices(models.TextChoices):
        PREPARATION = 'preparation', _('Preparation')
        ACTIVE = 'active', _('Active Composting')
        CURING = 'curing', _('Curing')
        READY = 'ready', _('Ready')
        USED = 'used', _('Used')


    volume = models.FloatField(help_text="Volume in cubic meters")

    composting_stage = models.CharField(
        _('Composting Stage'),
        max_length=50,
        choices=CompostingStageChoices.choices,
        default=CompostingStageChoices.PREPARATION,
    )
    last_turned_date = models.DateField(
        _('Last Turned Date'),
        null=True,
        blank=True,
        help_text=_("Date the compost pile was last turned or aerated."),
    )
    completion_date = models.DateField(
        _('Completion Date'),
        null=True,
        blank=True,
        help_text=_("Date the composting process was completed."),
    )
    temperature = models.FloatField(
        _('Temperature'),
        null=True,
        blank=True,
        help_text=_("Latest temperature reading in Celsius."),
    )
    moisture = models.FloatField(
        _('Moisture'),
        null=True,
        blank=True,
        help_text=_("Latest moisture level reading in percentage."),
    )
    ph = models.FloatField(
        _('pH'),
        null=True,
        blank=True,
        help_text=_("Latest pH reading."),
    )
    npk = models.CharField(
        _('NPK'),
        max_length=50,
        null=True,
        blank=True,
        validators=[validate_comma_separated_float_list],
        help_text=_("Enter NPK values as comma-separated floats (e.g., '10.5,15.2,25.0')."),
    )