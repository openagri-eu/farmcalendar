from django.conf import settings

from .base import *
from .builtin_activities import *


def get_generic_farm_calendar_activity_form(activity_type):
    activity_type_model_map = {
        settings.DEFAULT_CALENDAR_ACTIVITY_TYPES['fertilization']['name']: FertilizationOperation,
        settings.DEFAULT_CALENDAR_ACTIVITY_TYPES['irrigation']['name']: IrrigationOperation,
        settings.DEFAULT_CALENDAR_ACTIVITY_TYPES['crop_protection']['name']: CropProtectionOperation,
        settings.DEFAULT_CALENDAR_ACTIVITY_TYPES['crop_stress_indicator']['name']: CropStressIndicatorObservation,
        settings.DEFAULT_CALENDAR_ACTIVITY_TYPES['crop_growth_stage']['name']: CropGrowthStageObservation,
        settings.DEFAULT_CALENDAR_ACTIVITY_TYPES['compost_operation']['name']: CompostOperation,
        settings.DEFAULT_CALENDAR_ACTIVITY_TYPES['add_raw_material_operation']['name']: AddRawMaterialOperation,
        settings.DEFAULT_CALENDAR_ACTIVITY_TYPES['compost_turning_operation']['name']: CompostTurningOperation,
    }
    ActivityModel = activity_type_model_map[activity_type]
    ActivityForm = modelform_factory(
        ActivityModel,
        form=
    )


    return None