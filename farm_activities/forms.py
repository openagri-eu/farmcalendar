from django import forms
from django.conf import settings
from django.forms import modelform_factory
from .models import (
    FarmCalendarActivityType,
    FarmCalendarActivity,
    Observation,
    CompostOperation,
    AddRawMaterialOperation,
    FertilizationOperation,
    IrrigationOperation,
    CropProtectionOperation,
    CropStressIndicatorObservation,
    CropGrowthStageObservation,
    CropGrowthStageObservation,
)


class FarmCalendarActivityTypeForm(forms.ModelForm):
    class Meta:
        model = FarmCalendarActivityType
        fields = ['name', 'background_color', 'border_color', 'text_color']
        widgets = {
            'background_color': forms.TextInput(attrs={'class': 'color-picker'}),
            'border_color': forms.TextInput(attrs={'class': 'color-picker'}),
            'text_color': forms.TextInput(attrs={'class': 'color-picker'}),
        }


class FarmCalendarActivityForm(forms.ModelForm):
    class Meta:
        model = FarmCalendarActivity
        fields = ['activity_type', 'title', 'start_datetime', 'end_datetime', 'details']
        widgets = {
            'start_datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }


class GenericFarmCalendarActivityForm(forms.ModelForm):
    class Meta:
        model = FarmCalendarActivity
        exclude = ['id']
        fields = '__all__'
        widgets = {
            'start_datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'activity_type': forms.Select(attrs={'disabled': 'disabled'}),
        }


def get_generic_farm_calendar_activity_form(activity_type):
    activity_type_model_map = {
        settings.DEFAULT_CALENDAR_ACTIVITY_TYPES['fertilization']['name']: FertilizationOperation,
        settings.DEFAULT_CALENDAR_ACTIVITY_TYPES['irrigation']['name']: IrrigationOperation,
        settings.DEFAULT_CALENDAR_ACTIVITY_TYPES['crop_protection']['name']: CropProtectionOperation,
        settings.DEFAULT_CALENDAR_ACTIVITY_TYPES['crop_stress_indicator']['name']: CropStressIndicatorObservation,
        settings.DEFAULT_CALENDAR_ACTIVITY_TYPES['crop_growth_stage']['name']: CropGrowthStageObservation,
        settings.DEFAULT_CALENDAR_ACTIVITY_TYPES['compost_operation']['name']: CompostOperation,
        settings.DEFAULT_CALENDAR_ACTIVITY_TYPES['add_raw_material_operation']['name']: AddRawMaterialOperation,
    }
    ActivityModel = activity_type_model_map.get(activity_type)
    if ActivityModel is None:
        ActivityModel = FarmCalendarActivity

    exclude_fields = ['id']
    if activity_type != 'compost_operation':
        exclude_fields.append('nested_activities')

    GenericActivityForm = modelform_factory(
        ActivityModel,
        fields="__all__",
        exclude=exclude_fields,
        widgets={
            'start_datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'activity_type': forms.HiddenInput(),
            # 'end_datetime': forms.DateTimeInput(format='%Y-%m-%dT%H:%M:%S%z'),
            # 'end_datetime': forms.DateTimeInput(format='%Y-%m-%dT%H:%M:%S'),
            # 'end_datetime': forms.DateTimeInput(format='Y-m-d\\TH:i:sO' ),
        },
    )
    return GenericActivityForm


class FarmCalendarActivityTypeSelectionForm(forms.Form):
    activity_type = forms.ModelChoiceField(
        queryset=FarmCalendarActivityType.objects.all(),
        empty_label="Select Activity Type",
        required=True,
        label="Activity Type",
    )