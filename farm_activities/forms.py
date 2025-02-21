import json

from django.core.exceptions import ValidationError
from django import forms
from django.conf import settings
from django.forms import modelform_factory
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string
from django.urls import reverse

from dal import autocomplete


from .models import (
    FarmCalendarActivityType,
    FarmCalendarActivity,
    Observation,
    CompostOperation,
    AddRawMaterialOperation,
    AddRawMaterialCompostQuantity,
    FertilizationOperation,
    IrrigationOperation,
    CropProtectionOperation,
    CropStressIndicatorObservation,
    CropGrowthStageObservation,
    CompostTurningOperation,
)
from farm_management.models import CompostMaterial


class FarmCalendarActivityTypeForm(forms.ModelForm):
    class Meta:
        model = FarmCalendarActivityType
        fields = ['name', 'background_color', 'border_color', 'text_color']
        widgets = {
            'background_color': forms.TextInput(attrs={'class': 'color-picker'}),
            'border_color': forms.TextInput(attrs={'class': 'color-picker'}),
            'text_color': forms.TextInput(attrs={'class': 'color-picker'}),
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


def get_nested_activities_form(base_activity_form_cls):
    class CustomNestedActivityForm(base_activity_form_cls):
        nested_activities = forms.ModelMultipleChoiceField(
            queryset=FarmCalendarActivity.objects.none(),  # Default to empty queryset
            required=False,
            label="Nested Activities",
            widget=ReadOnlyNestedActivitiesWidget(),
        )

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            if self.instance and self.instance.pk:
                self.fields['nested_activities'].queryset = self.instance.nested_activities.all()
                self.initial['nested_activities'] = self.instance.nested_activities.all()

    return CustomNestedActivityForm


def get_parent_activity_form(base_activity_form_cls):
    class ParentActivityForm(base_activity_form_cls):
        parent_activity = forms.ModelChoiceField(
            queryset=FarmCalendarActivity.objects.all(),
            required=False,
            widget=autocomplete.ModelSelect2(url='activities-autocomplete', attrs={'class': 'select2'}),
            # forms.Select(attrs={'class': 'form-control'}),
            label="Part of Compost Operation"
        )

    return ParentActivityForm



class CompostMaterialsWidget(forms.widgets.Widget):
    template_name = "farm_activities/widgets/compost_materials_widgets.html"

    def __init__(self, attrs=None):
        super().__init__(attrs)

    def get_context(self, name, value, attrs):
        if value is None:
            value = []
        elif isinstance(value, str):
            try:
                value = json.loads(value)
            except json.JSONDecodeError:
                value = []

        return {
            "widget": {
                "name": name,
                "value": json.dumps(value),
                "attrs": self.build_attrs(attrs),
            }
        }
    def render(self, name, value, attrs=None, renderer=None):
        if value is None:
            value = []
        elif isinstance(value, str):
            try:
                value = json.loads(value)
                if value is None:
                    value = []
            except json.JSONDecodeError:
                value = []

        context = {
            "widget": {"name": name, "value": json.dumps(value)},
        }

        return mark_safe(render_to_string(self.template_name, context))


def get_raw_material_operation_form(nested_activity_form_cls):

    class RawMaterialNestedActivityForm(nested_activity_form_cls):
        compost_materials_json = forms.JSONField(
            label='Compost Materials',
            required=False,  # Make this field optional if needed
            widget=CompostMaterialsWidget()
        )

        class Meta:
            model = AddRawMaterialOperation
            # fields = nested_activity_form_cls.Meta.fields + ['compost_materials_json']
            exclude = nested_activity_form_cls.Meta.exclude + ['compost_materials']
            widgets = nested_activity_form_cls.Meta.widgets

        def __init__(self, *args, **kwargs):
            # Initialize the parent class first to set up the form fields
            super().__init__(*args, **kwargs)

            # Now, if there is an instance, populate the initial value for compost_materials_json
            if self.instance and self.instance.pk:
                # Prepare initial value for compost_materials_json from existing data
                initial_data = []
                compost_quantities = self.instance.compost_materials.through.objects.filter(operation=self.instance)

                for compost_quantity in compost_quantities:
                    initial_data.append({
                        'material_name': compost_quantity.material.name,  # Assuming the related `material` has a `name` field
                        'quantity': str(compost_quantity.applied_amount),
                        'unit': compost_quantity.applied_amount_unit,
                    })
                self.initial['compost_materials_json'] = initial_data

        def clean_compost_materials_json(self):
            data = self.cleaned_data.get('compost_materials_json')
            if not isinstance(data, list):
                raise ValidationError("The data should be a list of materials with quantity and unit.")

            for item in data:
                if not isinstance(item, dict):
                    raise ValidationError("Each item should be a dictionary.")
                if 'material_name' not in item or 'quantity' not in item or 'unit' not in item:
                    raise ValidationError("Each dictionary must have 'material_name', 'quantity', and 'unit'.")

            return data

        def save(self, commit=True):
            instance = super().save(commit=True)

            # Now, handle the intermediary model based on the JSON data
            compost_materials_data = self.cleaned_data.get('compost_materials_json', [])

            # Clear existing relationships (if any)
            instance.compost_materials.clear()

            for item in compost_materials_data:
                # Create the intermediary model objects from the JSON data
                AddRawMaterialCompostQuantity.objects.create(
                    operation=instance,
                    material=CompostMaterial.objects.get_or_create(name=item['material_name'])[0],  # Assuming 'material_name' corresponds to a Material model instance
                    applied_amount=item['quantity'],
                    applied_amount_unit=item['unit']
                )

            return instance


    return RawMaterialNestedActivityForm


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
    nested_compost_activities = [
        settings.DEFAULT_CALENDAR_ACTIVITY_TYPES['irrigation']['name'],
        settings.DEFAULT_CALENDAR_ACTIVITY_TYPES['compost_turning_operation']['name'],
        settings.DEFAULT_CALENDAR_ACTIVITY_TYPES['add_raw_material_operation']['name'],
    ]
    ActivityModel = activity_type_model_map.get(activity_type)
    is_observation = 'observation' in activity_type.lower()
    if ActivityModel is None:
        if is_observation:
            ActivityModel = Observation
        else:
            ActivityModel = FarmCalendarActivity

    exclude_fields = ['id',]
    if activity_type not in nested_compost_activities and not is_observation:
        exclude_fields.append('parent_activity')

    BaseGenericActivityForm = modelform_factory(
        ActivityModel,
        fields="__all__",
        exclude=exclude_fields,
        widgets={
            'start_datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'activity_type': forms.HiddenInput(),
            'nested_activities': ReadOnlyNestedActivitiesWidget(),  # Replace widget here
        },
    )

    GenericActivityForm = BaseGenericActivityForm
    # If the activity is "add_raw_material_operation", add a parent_activities field
    if activity_type == settings.DEFAULT_CALENDAR_ACTIVITY_TYPES['compost_operation']['name']:
        GenericActivityForm = get_nested_activities_form(BaseGenericActivityForm)

    if activity_type in nested_compost_activities:
        GenericNestedActivityForm = get_parent_activity_form(BaseGenericActivityForm)
        GenericActivityForm = GenericNestedActivityForm
        if activity_type == settings.DEFAULT_CALENDAR_ACTIVITY_TYPES['add_raw_material_operation']['name']:
            GenericActivityForm = get_raw_material_operation_form(GenericNestedActivityForm)

    return GenericActivityForm


class FarmCalendarActivityTypeSelectionForm(forms.Form):
    activity_type = forms.ModelChoiceField(
        queryset=FarmCalendarActivityType.objects.all(),
        empty_label="Select Activity Type",
        required=True,
        label="Activity Type",
    )