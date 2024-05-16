import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

from simple_history.models import HistoricalRecords


class DefaultAuthUserExtend(AbstractUser):
    class Meta:
        db_table = 'auth_user_extend'
        verbose_name = 'User Master'
        verbose_name_plural = 'User Masters'

    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    contact_no = models.CharField(max_length=10, null=True, db_index=True, default='', blank=True,
                                  validators=[RegexValidator(regex=r'^[0-9- ]+$', message="Invalid phone number")])
    token_version = models.IntegerField(default=1)

    history = HistoricalRecords(table_name="history_auth_user_extend")

    def __str__(self):
        return f"{self.email} {self.first_name}"

    # Add related_name to groups and user_permissions to avoid clashes
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name="user_extend_groups",
        related_query_name="user_extend",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="user_extend_permissions",
        related_query_name="user_extend",
    )


class FarmArea(models.Model):
    class Meta:
        db_table = "farm_areas"
        verbose_name = "Farm Area"
        verbose_name_plural = "Farm Areas"

    id = models.AutoField(primary_key=True, db_column='id', db_index=True, editable=False, unique=True,
                          blank=False, null=False, verbose_name='ID')

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    area_type = models.CharField(max_length=100, blank=True, null=True)
    size = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    unit = models.CharField(max_length=50, default='acre')

    status = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    history = HistoricalRecords(table_name="history_farm_areas")

    def __str__(self):
        return self.name


class FarmPlant(models.Model):
    class Meta:
        db_table = 'farm_plants'
        verbose_name = "Farm Plant"
        verbose_name_plural = "Farm Plants"

    id = models.AutoField(primary_key=True, db_column='id', db_index=True, editable=False, unique=True,
                          blank=False, null=False, verbose_name='ID')

    area = models.ForeignKey(FarmArea, on_delete=models.CASCADE, related_name='plants')
    species = models.CharField(max_length=255)
    variety = models.CharField(max_length=255, blank=True, null=True)
    planting_date = models.DateField()
    harvesting_date = models.DateField(blank=True, null=True)
    quantity = models.IntegerField(help_text="Quantity harvested")
    unit = models.CharField(max_length=50, default='kilograms')

    status = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    history = HistoricalRecords(table_name="history_farm_plants")

    def __str__(self):
        return f"{self.species} - {self.variety}"


class FarmAnimal(models.Model):
    class Meta:
        db_table = 'farm_animals'
        verbose_name = "Farm Animal"
        verbose_name_plural = "Farm Animals"

    id = models.AutoField(primary_key=True, db_column='id', db_index=True, editable=False, unique=True,
                          blank=False, null=False, verbose_name='ID')

    area = models.ForeignKey(FarmArea, on_delete=models.CASCADE, related_name='animals')
    species = models.CharField(max_length=255)
    breed = models.CharField(max_length=255, blank=True, null=True)
    birth_date = models.DateField()
    number_of_animals = models.IntegerField()

    status = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    history = HistoricalRecords(table_name="history_farm_animals")

    def __str__(self):
        return f"{self.species} - {self.breed}"


class FarmEquipment(models.Model):
    class Meta:
        db_table = 'farm_equipment'
        verbose_name = "Farm Equipment"
        verbose_name_plural = "Farm Equipment"

    id = models.AutoField(primary_key=True, db_column='id', db_index=True, editable=False, unique=True,
                          blank=False, null=False, verbose_name='ID')

    area = models.ForeignKey(FarmArea, on_delete=models.CASCADE, related_name='equipment')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    purchase_date = models.DateField()
    status = models.CharField(max_length=100, default='active')  # Status can be active, maintenance, decommissioned

    history = HistoricalRecords(table_name="history_farm_equipment")

    def __str__(self):
        return self.name

