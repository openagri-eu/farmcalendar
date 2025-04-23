from django import forms
from django.conf import settings
from django.forms import modelform_factory

from dal import autocomplete


def get_generic_farm_asset_form(model):
    GenericFarmAssetForm = modelform_factory(
        model,
        fields="__all__",
        exclude=['id', 'deleted_at'],
        widgets={
            'birth_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'purchase_date': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
            'animal_group': autocomplete.ListSelect2(url='animal-group-autocomplete'),

            'entry_date': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
            'leaving_date': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
            'previous_owner': forms.TextInput(attrs={'placeholder': 'Previous owner name'}),
        },
    )
    return GenericFarmAssetForm