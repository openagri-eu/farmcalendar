import json

from django.core.serializers import serialize
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import FormMixin, UpdateView
from django.conf import settings


from farm_management.models import Fertilizer, Pesticide
from farm_management.constants import ERROR_PROCESSING
from farm_management.forms import get_generic_treatment_materials_form


class BaseTreatmentMaterialsListManagementView(ListView, FormMixin, LoginRequiredMixin):
    model = None
    template_name = 'farm_management/farm_materials/treatment_materials.html'
    context_object_name = 'objects'
    success_url = None
    # success_url = reverse_lazy('fertilizers')
    asset_base_url = None
    # asset_base_url = reverse_lazy('fertilizers')
    form_class = None  # Form for creating/editing FarmAsset instances
    # form_class = get_generic_treatment_materials_form(Fertilizer)  # Form for creating/editing materials instances
    datatable_fields = ['name', 'active_substance', 'targeted_towards']

    def get_asset_base_api_url(self):
        asset_base_api_url = reverse_lazy(f'{self.model._meta.model_name}-list', kwargs={'version': settings.SHORT_API_VERSION})
        return asset_base_api_url

    def pre_serialize_query_set(self):
        queryset = self.get_queryset()
        return queryset

    def get_context_data(self, **kwargs):
        context = ListView.get_context_data(self, **kwargs)

        context['data_json'] = serialize('json', self.pre_serialize_query_set())

        form = self.get_form()

        context['form'] = form
        context['row_id_field'] = 'pk'  # Use 'pk' as the unique identifier
        context['asset_base_url'] = self.asset_base_url
        context['asset_base_api_url'] = self.get_asset_base_api_url()
        context['table_id'] = f'{self.model.__name__}Table'
        context['datatable_fields'] = self.datatable_fields
        context['model_name'] = self.model._meta.verbose_name
        context['id_edit'] = False

        return context

    def post(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        context = self.get_context_data()
        form = self.get_form()
        if form.is_valid():
            form.save()

            messages.success(request, f"{self.model.__name__} saved successfully.")
            return self.form_valid(form)
        messages.error(request, ERROR_PROCESSING)

        return self.render_to_response(context)

    def render_to_response(self, context, **response_kwargs):
        return super().render_to_response(context, **response_kwargs)


class BaseTreatmentMaterialUpdateView(UpdateView):
    model = None
    form_class = None
    # form_class = get_generic_farm_asset_form(FarmCrop)
    template_name = 'farm_management/farm_materials/treatment_materials.html'
    success_url = None
    # success_url = reverse_lazy('farm_crops')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_edit'] = True
        context['asset_base_url'] = self.success_url
        context['model_name'] = self.model._meta.verbose_name
        return context


class FertilizerUpdateView(BaseTreatmentMaterialUpdateView):
    model = Fertilizer
    form_class = get_generic_treatment_materials_form(Fertilizer)
    success_url = reverse_lazy('fertilizers')


class FertilizerListView(BaseTreatmentMaterialsListManagementView):
    model = Fertilizer
    success_url = reverse_lazy('fertilizers')
    asset_base_url = reverse_lazy('fertilizers')
    form_class = get_generic_treatment_materials_form(Fertilizer)
    datatable_fields = ['name', 'active_substance', 'nutrient_concentration', 'targeted_towards']


class PesticideUpdateView(BaseTreatmentMaterialUpdateView):
    model = Pesticide
    form_class = get_generic_treatment_materials_form(Fertilizer)
    success_url = reverse_lazy('fertilizers')


class PesticideListView(BaseTreatmentMaterialsListManagementView):
    model = Pesticide
    success_url = reverse_lazy('pesticides')
    asset_base_url = reverse_lazy('pesticides')
    form_class = get_generic_treatment_materials_form(Pesticide)
    datatable_fields = ['name', 'active_substance', 'preharvest_interval', 'targeted_towards']

