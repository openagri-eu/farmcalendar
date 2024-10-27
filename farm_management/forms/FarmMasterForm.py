from django import forms
from ..models import Farm


class FarmMasterForm(forms.ModelForm):
    # Including foreign key fields in the form
    admin_unit_l1 = forms.CharField(
        max_length=255, required=False, label="Admin Unit L1",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Greece'})
    )
    admin_unit_l2 = forms.CharField(
        max_length=255, required=False, label="Admin Unit L2",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Country X'})
    )
    address_area = forms.CharField(
        max_length=255, required=False, label="Address Area",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'District'})
    )
    municipality = forms.CharField(
        max_length=255, required=False, label="Municipality",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Municipality'})
    )
    community = forms.CharField(
        max_length=255, required=False, label="Community",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Community'})
    )
    locator_name = forms.CharField(
        max_length=255, required=False, label="Locator Name",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name of the place'})
    )

    class Meta:
        model = Farm
        fields = [
            'name', 'description', 'administrator',
            'contact_person_firstname', 'contact_person_lastname',
            'telephone', 'vat_id'
        ]
        labels = {
            'name': 'Farm Name',
            'description': 'Farm Description',
            'administrator': 'Farm Administrator',
            'contact_person_firstname': 'Contact Person First Name',
            'contact_person_lastname': 'Contact Person Last Name',
            'telephone': 'Contact Telephone',
            'vat_id': 'VAT ID',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Farm Name', 'label': 'Farm Name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Vineyard 219521', 'rows': 3}),
            'administrator': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Administrator'}),
            'contact_person_firstname': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Contact First Name'}),
            'contact_person_lastname': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Contact Last Name'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telephone'}),
            'vat_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'VAT ID'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:  # Editing an existing farm
            self.fields['name'].widget.attrs['readonly'] = True  # Make the name readonly if editing
