from django import forms
from django.forms import modelform_factory


from ..models import FarmCalendarActivityType, FarmCalendarActivity, Observation
from .widgets import ReadOnlyNestedActivitiesWidget


class FarmCalendarActivityTypeSelectionForm(forms.Form):
    activity_type = forms.ModelChoiceField(
        queryset=FarmCalendarActivityType.objects.all(),
        empty_label="Select Activity Type",
        required=True,
        label="Activity Type",
    )


class FarmCalendarActivityTypeForm(forms.ModelForm):
    class Meta:
        model = FarmCalendarActivityType
        fields = ["name", "background_color", "border_color", "text_color"]
        widgets = {
            "background_color": forms.TextInput(attrs={"class": "color-picker"}),
            "border_color": forms.TextInput(attrs={"class": "color-picker"}),
            "text_color": forms.TextInput(attrs={"class": "color-picker"}),
        }


class FarmCalendarActivityForm(forms.ModelForm):
    class Meta:
        model = FarmCalendarActivity
        fields = [
            "activity_type",
            "title",
            "start_datetime",
            "end_datetime",
            "details",
            "responsible_agent",
            "agricultural_machinery",
            # "parent_activity",
        ]
        widgets={
            "start_datetime": forms.DateTimeInput(attrs={"type": "datetime-local"}),
            "end_datetime": forms.DateTimeInput(attrs={"type": "datetime-local"}),
            "activity_type": forms.HiddenInput(),
            # "nested_activities": ReadOnlyNestedActivitiesWidget(),
        },


class ObservationForm(FarmCalendarActivityForm):
    class Meta:
        model = Observation
        fields = FarmCalendarActivityForm.Meta.fields + ['parent_activitiy']
        widgets = {
            "background_color": forms.TextInput(attrs={"class": "color-picker"}),
            "border_color": forms.TextInput(attrs={"class": "color-picker"}),
            "text_color": forms.TextInput(attrs={"class": "color-picker"}),
        }


class ParentActivityForm(FarmCalendarActivityForm):
    nested_activities = forms.ModelMultipleChoiceField(
        queryset=FarmCalendarActivity.objects.none(),  # Default to empty queryset
        required=False,
        label="Nested Activities",
        widget=ReadOnlyNestedActivitiesWidget(),
    )
    class Meta:
        widgets = FarmCalendarActivityForm.Meta.widgets.copy()
        widgets.update(
            {
                'nested_activities': ReadOnlyNestedActivitiesWidget(),
            })

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance and self.instance.pk:
            self.fields['nested_activities'].queryset = self.instance.nested_activities.all()
            self.initial['nested_activities'] = self.instance.nested_activities.all()


class NestedActivityForm(FarmCalendarActivityForm):
    parent_activity = forms.ModelChoiceField(
        queryset=FarmCalendarActivity.objects.all(),
        required=False,
        widget=autocomplete.ModelSelect2(url='activities-autocomplete', attrs={'class': 'select2'}),
        label="Part of Activity"
    )
