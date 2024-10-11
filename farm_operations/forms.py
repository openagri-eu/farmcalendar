from django import forms
from .models import FarmOperationType, FarmOperation


class FarmOperationTypeForm(forms.ModelForm):
    class Meta:
        model = FarmOperationType
        fields = ['name', 'background_color', 'border_color', 'text_color']
        widgets = {
            'background_color': forms.TextInput(attrs={'class': 'color-picker'}),
            'border_color': forms.TextInput(attrs={'class': 'color-picker'}),
            'text_color': forms.TextInput(attrs={'class': 'color-picker'}),
        }


class FarmOperationForm(forms.ModelForm):
    class Meta:
        model = FarmOperation
        fields = ['operation_type', 'title', 'start_datetime', 'end_datetime', 'details']
        widgets = {
            'start_datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
