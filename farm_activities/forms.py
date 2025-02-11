from django import forms
from django.conf import settings
from django.forms import modelform_factory
from django.utils.safestring import mark_safe
from django.urls import reverse

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


class ReadOnlyNestedActivitiesWidget(forms.Widget):
    def render(self, name, value, attrs=None, renderer=None):
        # Check if there are any nested activities
        if value:
            actual_value = self.choices.queryset.filter(pk__in=value)
            # Create a Bootstrap-styled list with links
            list_items = [
                f'<li class="list-group-item">'
                f'<a href="{reverse("calendar_activity_edit", kwargs={"pk": act.pk})}" class="text-decoration-none">'
                f'{act}</a></li>'
                for act in actual_value  # Assuming `value` is a queryset of nested activities
            ]

            # Wrap the list items in a Bootstrap unordered list
            return mark_safe(
                f'<ul class="list-group">{"" .join(list_items)}</ul>'
            )
        return mark_safe("<p>No nested activities</p>")


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
    if activity_type != settings.DEFAULT_CALENDAR_ACTIVITY_TYPES['compost_operation']['name']:
        exclude_fields.append('nested_activities')

    BaseGenericActivityForm = modelform_factory(
        ActivityModel,
        fields="__all__",
        exclude=exclude_fields,
        widgets={
            'start_datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'activity_type': forms.HiddenInput(),
            'nested_activities': ReadOnlyNestedActivitiesWidget(),  # Replace widget here

            # 'end_datetime': forms.DateTimeInput(format='%Y-%m-%dT%H:%M:%S%z'),
            # 'end_datetime': forms.DateTimeInput(format='%Y-%m-%dT%H:%M:%S'),
            # 'end_datetime': forms.DateTimeInput(format='Y-m-d\\TH:i:sO' ),
        },
    )

    GenericActivityForm = BaseGenericActivityForm
    # If the activity is "add_raw_material_operation", add a parent_activities field
    nested_compost_activities = [
        settings.DEFAULT_CALENDAR_ACTIVITY_TYPES['irrigation']['name'],
        settings.DEFAULT_CALENDAR_ACTIVITY_TYPES['add_raw_material_operation']['name']
    ]
    if activity_type in nested_compost_activities:
        class CustomActivityForm(BaseGenericActivityForm):
            parent_activities = forms.ModelChoiceField(
                queryset=CompostOperation.objects.all(),
                required=False,
                widget=forms.Select(attrs={'class': 'form-control'}),
                label="Part of compost Operation"
            )

            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                if self.instance and self.instance.pk:
                    self.fields['parent_activities'].initial = self.instance.parent_activities.first()

            def save(self, commit=True):
                instance = super().save(commit=False)

                if commit:
                    instance.save()  # Save instance before modifying M2M fields

                if 'parent_activities' in self.cleaned_data:
                    compost_op = self.cleaned_data['parent_activities']
                    if compost_op:
                        instance.parent_activities.set([compost_op])  # Correctly assign parent CompostOperation

                return instance

        GenericActivityForm = CustomActivityForm
    return GenericActivityForm


class FarmCalendarActivityTypeSelectionForm(forms.Form):
    activity_type = forms.ModelChoiceField(
        queryset=FarmCalendarActivityType.objects.all(),
        empty_label="Select Activity Type",
        required=True,
        label="Activity Type",
    )