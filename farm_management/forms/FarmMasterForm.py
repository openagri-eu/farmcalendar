from django import forms
from ..models import FarmMaster


class FarmMasterForm(forms.ModelForm):
    class Meta:
        model = FarmMaster
        fields = [
            'name', 'description', 'administrator',
            'contact_person_firstname', 'contact_person_lastname',
            'telephone', 'vat_id',
            'admin_unit_l1', 'admin_unit_l2', 'address_area',
            'municipality', 'community', 'locator_name'
        ]
        widgets = {
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Vineyard 219521',
                'style': 'width: 100%; height: 100px; overflow-y: scroll;'
            }),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Farm Name', 'label': 'Farm Name'}),
            'administrator': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Administrator'}),
            'contact_person_firstname': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Contact First Name'}),
            'contact_person_lastname': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Contact Last Name'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telephone'}),
            'vat_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'VAT ID'}),
            'admin_unit_l1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Greece'}),
            'admin_unit_l2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Country X'}),
            'address_area': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'District'}),
            'municipality': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Municipality'}),
            'community': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Community'}),
            'locator_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name of the place'}),
        }

