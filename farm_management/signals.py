from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import BaseModel


@receiver(post_save, sender=BaseModel)
def cascade_soft_delete(sender, instance, **kwargs):
    if instance.status == instance.BaseModelStatus.DELETED:
        # Loop through all related objects
        for related in instance._meta.related_objects:
            # Access the related manager or object
            related_name = related.get_accessor_name()
            related_manager = getattr(instance, related_name)

            # For ForeignKey or ManyToManyField relationships
            if isinstance(related_manager, models.Manager):
                for related_obj in related_manager.all():
                    if isinstance(related_obj, BaseModel) and related_obj.status != BaseModel.BaseModelStatus.DELETED:
                        related_obj.soft_delete()
            # For OneToOneField relationships
            else:
                if isinstance(related_manager, BaseModel) and related_manager.status != BaseModel.BaseModelStatus.DELETED:
                    related_manager.soft_delete()