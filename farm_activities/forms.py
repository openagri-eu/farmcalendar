from django import forms
from .models import FarmCalendarActivityType, FarmCalendarActivity


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
