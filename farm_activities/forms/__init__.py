from django.conf import settings

from .base import *
from .builtin_activities import *


def get_generic_farm_calendar_activity_form(activity_type):
    activity_type_modelform_map = {
        settings.DEFAULT_CALENDAR_ACTIVITY_TYPES['fertilization']['name']: FertilizationOperationForm,
        settings.DEFAULT_CALENDAR_ACTIVITY_TYPES['irrigation']['name']: IrrigationOperationForm,
        settings.DEFAULT_CALENDAR_ACTIVITY_TYPES['crop_protection']['name']: CropProtectionOperationForm,
        settings.DEFAULT_CALENDAR_ACTIVITY_TYPES['crop_stress_indicator']['name']: CropStressIndicatorObservationForm,
        settings.DEFAULT_CALENDAR_ACTIVITY_TYPES['crop_growth_stage']['name']: CropGrowthStageObservationForm,
        settings.DEFAULT_CALENDAR_ACTIVITY_TYPES['compost_operation']['name']: CompostOperationForm,
        settings.DEFAULT_CALENDAR_ACTIVITY_TYPES['add_raw_material_operation']['name']: AddRawMaterialOperationForm,
        settings.DEFAULT_CALENDAR_ACTIVITY_TYPES['compost_turning_operation']['name']: CompostTurningOperationForm,
    }

    ActivityModelForm = activity_type_modelform_map.get(activity_type)
    is_observation = 'observation' in activity_type.lower()
    if ActivityModelForm is None:
        if is_observation:
            ActivityModelForm = ObservationForm
        else:
            ActivityModelForm = FarmCalendarActivityForm

    return ActivityModelForm