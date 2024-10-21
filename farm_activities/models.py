from django.db import models
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
    name = models.CharField(max_length=100)
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
        default='#ffffff',  # Default text color
    )

    def __str__(self):
        return self.name


class FarmCalendarActivity(models.Model):
    """
    An occurrence of some farm activity on the calendar.
    This will be the base for both the operations and observations, as in
    how they are presented in a calendar and what type of activity (or event) this is about.
    """
    activity_type = models.ForeignKey(FarmCalendarActivityType, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(blank=True, null=True)
    details = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} ({self.start_time.strftime('%Y-%m-%d %H:%M')})"


class FertilizationOperation(FarmCalendarActivity):
    # treated_area = models.IntegerField(blank=True, null=True)
    # fertilization_type = models.CharField(max_length=255, blank=True, null=True)
    applied_amount = models.DecimalField(max_digits=10, decimal_places=2)
    applied_amount_unit = models.CharField(max_length=255)
    application_method = models.CharField(max_length=255, blank=True, null=True)

    operated_on = models.ForeignKey('farm_management.FarmParcel', on_delete=models.CASCADE)
    fertilizer = models.ForeignKey('farm_management.Fertilizer', on_delete=models.SET_NULL, blank=True, null=True)
    # TreatmentPlan
    def save(self, *args, **kwargs):
        self.activity_type, _ = FarmCalendarActivityType.objects.get_or_create(name=settings.DEFAULT_CALENDAR_ACTIVITY_TYPES['fertilization']['name'])
        super().save(*args, **kwargs)


