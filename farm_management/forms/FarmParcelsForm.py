from django import forms
from ..models import FarmParcel


class FarmParcelsForm(forms.ModelForm):
    class Meta:
        model = FarmParcel
        fields = ['farm', 'geo_id', 'description', 'coordinates', 'area', 'category']
