from django.db import models
from django.core.validators import RegexValidator

from django.conf import settings


class FarmOperationType(models.Model):
    id = models.AutoField(primary_key=True, db_index=True, editable=False, unique=True,
                          blank=False, null=False, verbose_name='ID')

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


class FarmOperation(models.Model):
    id = models.AutoField(primary_key=True, db_index=True, editable=False, unique=True,
                          blank=False, null=False, verbose_name='ID')

    title = models.CharField(max_length=200)
    details = models.TextField(blank=True, null=True)

    operation_type = models.ForeignKey(FarmOperationType, on_delete=models.CASCADE)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()

    responsible_agent = models.CharField(blank=True, null=True)
    agricultural_machinery = models.ManyToManyField('farm_management.AgriculturalMachine', related_name='used_in_operations', blank=True, null=True)
    # weather_observation = models.ManyToManyField('farm_management.AgriculturalMachine', related_name='used_in_operations', blank=True, null=True)?

    def __str__(self):
        return f"{self.title} ({self.start_time.strftime('%Y-%m-%d %H:%M')})"


class FertilizationOperation(FarmOperation):
    # treated_area = models.IntegerField(blank=True, null=True)
    # fertilization_type = models.CharField(max_length=255, blank=True, null=True)
    applied_amount = models.DecimalField(max_digits=10, decimal_places=2)
    applied_amount_unit = models.CharField(max_length=255)
    application_method = models.CharField(max_length=255, blank=True, null=True)

    operated_on = models.ForeignKey('farm_management.FarmParcel', on_delete=models.CASCADE)
    fertilizer = models.ForeignKey('farm_management.Fertilizer', on_delete=models.SET_NULL, blank=True, null=True)
    # TreatmentPlan
    def save(self, *args, **kwargs):
        self.operation_type, _ = FarmOperationType.objects.get_or_create(name=settings.DEFAULT_OPERATION_TYPES['fertilization']['name'])
        super().save(*args, **kwargs)


