from django import forms
from .models import FarmActivityType, FarmActivity


class FarmActivityTypeForm(forms.ModelForm):
    class Meta:
        model = FarmActivityType
        fields = ['name', 'background_color', 'border_color', 'text_color']
        widgets = {
            'background_color': forms.TextInput(attrs={'class': 'color-picker'}),
            'border_color': forms.TextInput(attrs={'class': 'color-picker'}),
            'text_color': forms.TextInput(attrs={'class': 'color-picker'}),
        }


class FarmActivityForm(forms.ModelForm):
    class Meta:
        model = FarmActivity
        fields = ['activity_type', 'title', 'start_time', 'end_time', 'details']
        widgets = {
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
