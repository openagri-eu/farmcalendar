from django.core.validators import (RegexValidator)
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from simple_history.models import HistoricalRecords


class BaseModel(models.Model):
    class BaseModelStatus(models.IntegerChoices):
        INACTIVE = 0, 'Inactive'
        ACTIVE = 1, 'Active'
        DELETED = 2, 'Deleted'

    id = models.AutoField(primary_key=True, db_column='id', db_index=True, editable=False, unique=True, blank=False,
                          null=False, verbose_name='ID')

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
        # self.save()

        # Perform cascading soft delete on related objects
        for related in self._meta.related_objects:
            related_name = related.get_accessor_name()
            related_manager_or_obj = getattr(self, related_name, None)

            # For ForeignKey or ManyToMany relationships
            if isinstance(related_manager_or_obj, models.Manager):
                for related_obj in related_manager_or_obj.all():
                    if hasattr(related_obj, 'soft_delete') and related_obj.status != self.BaseModelStatus.DELETED:
                        # Check if the related object is shared by other instances
                        is_shared = related.related_model.objects.filter(
                            **{related.field.name: related_obj}).exclude(pk=self.pk).exists()
                        if not is_shared:
                            related_obj.soft_delete()
            # For OneToOne relationships
            elif isinstance(related_manager_or_obj,
                            BaseModel) and related_manager_or_obj.status != self.BaseModelStatus.DELETED:
                # Check if the OneToOneField instance is shared by any other model or object
                is_shared = type(related_manager_or_obj).objects.filter(pk=related_manager_or_obj.pk).exclude(
                    farm=self.pk).exists()  # Adjust `farm` based on your actual foreign key name if necessary
                if not is_shared:
                    related_manager_or_obj.soft_delete()


class ActivePageManager(models.Manager):
    def get_queryset(self):
        # Exclude records with status set to DELETED (status=2)
        return super().get_queryset().filter(status__lt=BaseModel.BaseModelStatus.DELETED)


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
                                   validators=[RegexValidator(regex=r'^[a-zA-Z0-9\s-]+$',
                                                              message="Invalid characters")])
    menu_order = models.SmallIntegerField(null=True, blank=True)

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
