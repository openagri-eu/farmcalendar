from django.core.validators import (RegexValidator)
from django.db import models
from django.utils.translation import gettext_lazy as _

from simple_history.models import HistoricalRecords


class BaseModel(models.Model):
    status = models.BooleanField(default=True, verbose_name='Status')
    deleted = models.BooleanField(default=False, verbose_name='Is Deleted')
    deleted_at = models.DateTimeField(null=True, blank=True, verbose_name='Deleted At')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated At')

    class Meta:
        abstract = True


class AdminMenuMaster(BaseModel):
    id = models.SmallAutoField(primary_key=True, db_column='id', db_index=True, editable=False, unique=True,
                               blank=False, null=False, verbose_name='ID')
    parent_id = models.ForeignKey('self', null=True, blank=True, related_name='submenus', db_column='parent_id',
                                  on_delete=models.CASCADE)
    menu_name = models.CharField(max_length=30, null=False, blank=False, unique=True,
                                 validators=[RegexValidator(regex=r'^[a-zA-Z0-9()\s]+$', message="Invalid characters")])
    menu_icon = models.CharField(max_length=20, null=True, blank=True, default='list',
                                 validators=[RegexValidator(regex=r'^[a-z0-9-]+$', message="Invalid characters")])
    menu_route = models.CharField(max_length=30, null=True, blank=True,
                                  validators=[RegexValidator(regex=r'^[a-zA-Z0-9\s-]+$', message="Invalid characters")])
    menu_access = models.CharField(max_length=30, null=True, blank=True,
                                   validators=[RegexValidator(regex=r'^[a-zA-Z0-9\s-]+$', message="Invalid characters")])
    menu_order = models.SmallIntegerField(null=True, blank=True,
                                          validators=[RegexValidator(regex=r'^[0-9]+$', message="Invalid characters")])

    def __str__(self):
        return f"{self.menu_name} ({self.menu_route})"

    class Meta:
        db_table = "admin_menu_master"
        verbose_name = "Admin Menu"
        verbose_name_plural = "Admin Menus"


class NamedHistoricalBaseModel(models.Model):
    id = models.AutoField(primary_key=True, db_index=True, editable=False, unique=True,
                          blank=False, null=False, verbose_name='ID')

    name = models.CharField(max_length=100)

    class StatusChoices(models.IntegerChoices):
        ACTIVE = 0, _('Active')
        DELETED = 1, _('Deleted')

    status = models.IntegerField(choices=StatusChoices, default=StatusChoices.ACTIVE)
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    history = HistoricalRecords(inherit=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name
