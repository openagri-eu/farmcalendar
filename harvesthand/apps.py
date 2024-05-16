from django.apps import AppConfig


class HarvesthandConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'harvesthand'
    verbose_name = 'Harvest Hand'

    def ready(self):
        import harvesthand.signals
