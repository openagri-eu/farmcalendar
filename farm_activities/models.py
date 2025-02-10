import uuid
import datetime
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models import Q
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator

from django.conf import settings


class FarmCalendarActivityType(models.Model):
    """
    This refers to a generic types of activity that is displayed on the farm calendar.
    It is used to represent both observation types and operation types,
    with a descrition of what is this type of activity, and the colors that should be used
    to represent this in the calendar.
    The list of default farm activity types is set on settings.DEFAULT_CALENDAR_ACTIVITY_TYPES.
    These default types are main activity types (observations and operations) already identified
    during development. However, the user may add their own generic activity type that is not
    covered by the defaults.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, db_index=True, editable=False, unique=True,
                          blank=False, null=False, verbose_name='ID')
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    # Fields for color codes
    background_color = models.CharField(
        max_length=7,
        validators=[RegexValidator(regex='^#[0-9A-Fa-f]{6}$', message='Enter a valid hex color code.')],
        default='#007bff',  # Default color
    )
    border_color = models.CharField(
        max_length=7,
        validators=[RegexValidator(regex='^#[0-9A-Fa-f]{6}$', message='Enter a valid hex color code.')],
        default='#007bff',  # Default color
    )
    text_color = models.CharField(
        max_length=7,
        validators=[RegexValidator(regex='^#[0-9A-Fa-f]{6}$', message='Enter a valid hex color code.')],
        default='#000000',  # Default text color
    )

    def __str__(self):
        return self.name


class FarmCalendarActivity(models.Model):
    """
    An occurrence of some farm activity on the calendar.
    This will be the base for both the operations and observations, as in
    how they are presented in a calendar and what type of activity (or event) this is about.
    """
    class Meta:
        verbose_name = "Farm Activity"
        verbose_name_plural = "Farm Activities"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, db_index=True, editable=False, unique=True,
                          blank=False, null=False, verbose_name='ID')

    activity_type = models.ForeignKey(FarmCalendarActivityType, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    start_datetime = models.DateTimeField(default=datetime.datetime.now)
    end_datetime = models.DateTimeField(blank=True, null=True)

    details = models.TextField(blank=True, null=True)

    responsible_agent = models.CharField(blank=True, null=True)
    # need to change this into a operation model instead...
    agricultural_machinery = models.ManyToManyField('farm_management.AgriculturalMachine', related_name='used_in_operations', blank=True)
    # weather_observation = models.ManyToManyField('farm_management.AgriculturalMachine', related_name='used_in_operations', blank=True, null=True)?

    def __str__(self):
        return f"{self.title} ({self.start_datetime.strftime('%Y-%m-%d %H:%M')})"


class FertilizationOperation(FarmCalendarActivity):
    class Meta:
        verbose_name = "Fertilization Operation"
        verbose_name_plural = "Fertilization Operations"

    # treated_area = models.IntegerField(blank=True, null=True)
    # fertilization_type = models.CharField(max_length=255, blank=True, null=True)
    applied_amount = models.DecimalField(max_digits=10, decimal_places=2)
    applied_amount_unit = models.CharField(max_length=255)

    application_method = models.CharField(max_length=255, blank=True, null=True)

    operated_on = models.ForeignKey('farm_management.FarmParcel', on_delete=models.CASCADE)
    fertilizer = models.ForeignKey('farm_management.Fertilizer', on_delete=models.SET_NULL, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.activity_type, _ = FarmCalendarActivityType.objects.get_or_create(name=settings.DEFAULT_CALENDAR_ACTIVITY_TYPES['fertilization']['name'])
        super().save(*args, **kwargs)



class IrrigationOperation(FarmCalendarActivity):

    class Meta:
        verbose_name = "Irrigation Operation"
        verbose_name_plural = "Irrigation Operations"

    class IrrigationSystemChoices(models.TextChoices):
        SPRINKLER = 'sprinkler', _('Sprinkler')
        DRIP = 'drip', _('Drip')
        CENTRE_PIVOT  = 'centre_pivot', _('Centre Pivot')
        FURROW  = 'furrow', _('Furrow')
        TERRACED  = 'terraced', _('Terraced')

    applied_amount = models.DecimalField(max_digits=10, decimal_places=2)
    applied_amount_unit = models.CharField(max_length=255)

    operated_on = models.ForeignKey('farm_management.FarmParcel', on_delete=models.CASCADE)

    irrigation_system = models.CharField(max_length=50, choices=IrrigationSystemChoices.choices,
                                        default=IrrigationSystemChoices.SPRINKLER)

    def save(self, *args, **kwargs):
        self.activity_type, _ = FarmCalendarActivityType.objects.get_or_create(name=settings.DEFAULT_CALENDAR_ACTIVITY_TYPES['irrigation']['name'])
        super().save(*args, **kwargs)



class CropProtectionOperation(FarmCalendarActivity):

    class Meta:
        verbose_name = "Crop Protection Operation"
        verbose_name_plural = "Crop Protection Operations"


    applied_amount = models.DecimalField(max_digits=10, decimal_places=2)
    applied_amount_unit = models.CharField(max_length=255)

    operated_on = models.ForeignKey('farm_management.FarmParcel', on_delete=models.CASCADE)
    pesticide = models.ForeignKey('farm_management.Pesticide', on_delete=models.SET_NULL, blank=True, null=True)


    def save(self, *args, **kwargs):
        self.activity_type, _ = FarmCalendarActivityType.objects.get_or_create(name=settings.DEFAULT_CALENDAR_ACTIVITY_TYPES['crop_protection']['name'])
        super().save(*args, **kwargs)


class Observation(FarmCalendarActivity):
    class Meta:
        verbose_name = "Observation"
        verbose_name_plural = "Observations"

    value = models.CharField(max_length=255)
    value_unit = models.CharField(max_length=255, blank=True, null=True)
    observed_property = models.CharField(max_length=255)


class CropStressIndicatorObservation(Observation):

    class Meta:
        verbose_name = "Crop Stress Indicator Observation"
        verbose_name_plural = "Crop Stress Indicator Observations"

    crop = models.ForeignKey('farm_management.FarmCrop', on_delete=models.CASCADE, blank=False, null=False)

    def save(self, *args, **kwargs):
        self.activity_type, _ = FarmCalendarActivityType.objects.get_or_create(name=settings.DEFAULT_CALENDAR_ACTIVITY_TYPES['crop_stress_indicator']['name'])
        super().save(*args, **kwargs)


class CropGrowthStageObservation(Observation):

    class Meta:
        verbose_name = "Crop Growth Stage Observation"
        verbose_name_plural = "Crop Growth Stage Observations"

    crop = models.ForeignKey('farm_management.FarmCrop', on_delete=models.CASCADE, blank=False, null=False)

    def save(self, *args, **kwargs):
        self.activity_type, _ = FarmCalendarActivityType.objects.get_or_create(name=settings.DEFAULT_CALENDAR_ACTIVITY_TYPES['crop_growth_stage']['name'])
        # todo: fix this so that only change if this is the latest observation from that crop
        self.crop.growth_stage = self.value
        self.crop.save()
        super().save(*args, **kwargs)