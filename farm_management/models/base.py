from django.db import models
from django.utils.translation import gettext_lazy as _

from simple_history.models import HistoricalRecords


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
