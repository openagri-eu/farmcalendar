from django.db import models
from django.core.validators import RegexValidator

from django.conf import settings


class FarmOperationType(models.Model):
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
    operation_type = models.ForeignKey(FarmOperationType, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    details = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} ({self.start_time.strftime('%Y-%m-%d %H:%M')})"


# class FertilizationOperation(FarmOperation):
#     treated_area = models.IntegerField(blank=True, null=True)
#     application_method = models.CharField(max_length=255, blank=True, null=True)
#     fertilization_type = models.CharField(max_length=255, blank=True, null=True)
#     fertilizer = models.ForeignKey('farm_management.Fertilizer', on_delete=models.SET_NULL, blank=True, null=True)
#     def save(self, *args, **kwargs):
#         # Set activity_type to Fertilization automatically
#         self.activity_type, _ = FarmOperationType.get_or_create(name=settings.DEFAULT_OPERATION_TYPES['fertilization']['name'])
#         super().save(*args, **kwargs)


