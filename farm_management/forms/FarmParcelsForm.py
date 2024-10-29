from django import forms
from ..models import FarmParcel, FarmMaster


class FarmParcelsForm(forms.ModelForm):
    # Adding farm selection as a ModelChoiceField
    farm = forms.ModelChoiceField(
        queryset=FarmMaster.active_objects.all(),
        required=True,
        label="Select Farm",
        widget=forms.Select(attrs={'class': 'form-control', 'required': 'required'})
    )

    identifier = forms.CharField(
        max_length=100, required=True, label="Parcel Identifier",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Identifier for the parcel'})
    )

    description = forms.CharField(
        required=False, label="Description",
        widget=forms.Textarea(attrs={
            'class': 'form-control', 'placeholder': 'Description of the parcel',
            'style': 'width: 100%; height: 100px; overflow-y: scroll;'
        })
    )

    category = forms.ChoiceField(
        choices=FarmParcel.CultivationTypeChoices.choices,
        required=True, label="Cultivation Type",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    valid_from = forms.DateTimeField(
        required=False, label="Valid From",
        widget=forms.DateTimeInput(attrs={'class': 'form-control',
                                          'placeholder': 'YYYY-MM-DD HH:MM:SS'})
    )
    valid_to = forms.DateTimeField(
        required=False, label="Valid To",
        widget=forms.DateTimeInput(attrs={'class': 'form-control',
                                          'placeholder': 'YYYY-MM-DD HH:MM:SS'})
    )
    in_region = forms.CharField(
        max_length=255, required=False, label="Region",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Region name'})
    )
    has_toponym = forms.CharField(
        max_length=255, required=False, label="Toponym",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Toponym of the area'})
    )
    area = forms.DecimalField(
        max_digits=15, decimal_places=2, required=False, label="Area (sq. meters)",
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0.0', 'value': 0.0})
    )
    is_nitro_area = forms.BooleanField(
        required=False, label="Nitro Area",
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    is_natura2000_area = forms.BooleanField(
        required=False, label="Natura 2000 Area",
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    is_pdopg_area = forms.BooleanField(
        required=False, label="PDOPG Area",
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    is_irrigated = forms.BooleanField(
        required=False, label="Irrigated",
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    is_cultivated_in_levels = forms.BooleanField(
        required=False, label="Cultivated in Levels",
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    is_ground_slope = forms.BooleanField(
        required=False, label="Ground Slope",
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    depiction = forms.URLField(
        required=False, label="Depiction URL",
        widget=forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Image or map URL'})
    )
    irrigation_flow = forms.FloatField(
        required=False, label="Irrigation Flow (units)",
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Flow rate'})
    )
    geo_id = forms.UUIDField(
        required=False, label="Geographic Data ID",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Geographic UUID'})
    )
    coordinates = forms.CharField(
        max_length=255, required=False, label="Coordinates",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Latitude, Longitude'})
    )

    class Meta:
        model = FarmParcel
        fields = [
            'farm', 'identifier', 'description', 'category', 'valid_from', 'valid_to', 'in_region', 'has_toponym',
            'area', 'is_nitro_area', 'is_natura2000_area', 'is_pdopg_area', 'is_irrigated',
            'is_cultivated_in_levels', 'is_ground_slope', 'depiction', 'irrigation_flow', 'geo_id', 'coordinates'
        ]
