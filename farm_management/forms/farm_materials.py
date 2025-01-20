from django import forms
from django.conf import settings
from django.forms import modelform_factory

def get_generic_treatment_materials_form(model):
    GenericTreatmentMaterialsForm = modelform_factory(
        model,
        fields="__all__",
        exclude=['id', 'deleted_at'],
    )
    return GenericTreatmentMaterialsForm