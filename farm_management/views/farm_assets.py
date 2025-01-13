import json

from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.edit import FormMixin, UpdateView
from django.conf import settings


from farm_management.models import FarmAsset, FarmCrop, FarmAnimal, AgriculturalMachine
from farm_management.constants import ERROR_PROCESSING
from farm_management.forms import get_generic_farm_asset_form



class BaseFarmAssetListManagementView(ListView, FormMixin, LoginRequiredMixin):
    model = FarmAsset
    template_name = "farm_management/farm_assets/farm_assets.html"
    context_object_name = 'objects'
    success_url = reverse_lazy('FarmAsset')
    asset_base_url = reverse_lazy('farm_assets')
    form_class = None  # Form for creating/editing FarmAsset instances
    # form_class = get_generic_farm_asset_form(FarmCrops)  # Form for creating/editing FarmAsset instances
    datatable_fields = ['name', 'parcel']

    def get_asset_base_api_url(self):
        asset_base_api_url = reverse_lazy(f'{self.model._meta.model_name}-list', kwargs={'version': settings.SHORT_API_VERSION})
        return asset_base_api_url

    def pre_serialize_query_set(self):
        queryset = self.get_queryset()
        queryset = queryset.select_related('parcel')

        annotated_data = []
        for obj in queryset:
            farm_parcel_str = str(obj.parcel)

            fields = {field.name: str(getattr(obj, field.name)) for field in obj._meta.fields}
            fields['status'] = obj.status
            fields['parcel'] = str(farm_parcel_str)
            # Add the object data, including the related FarmParcel name
            annotated_data.append({
                'pk': str(obj.pk),
                'fields': fields,
            })
        return annotated_data

    def get_context_data(self, **kwargs):
        context = ListView.get_context_data(self, **kwargs)

        context['data_json'] = json.dumps(list(self.pre_serialize_query_set()))

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


class BaseFarmAssetUpdateView(UpdateView):
    model = None
    form_class = None
    # form_class = get_generic_farm_asset_form(FarmCrop)
    template_name = 'farm_management/farm_assets/farm_crops.html'
    success_url = reverse_lazy('farm_crops')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_edit'] = True
        context['asset_base_url'] = self.success_url
        context['model_name'] = self.model._meta.verbose_name
        return context


class FarmCropUpdateView(BaseFarmAssetUpdateView):
    model = FarmCrop
    form_class = get_generic_farm_asset_form(FarmCrop)
    template_name = 'farm_management/farm_assets/farm_assets.html'
    success_url = reverse_lazy('farm_crops')


class FarmCropListView(BaseFarmAssetListManagementView):
    model = FarmCrop
    template_name = "farm_management/farm_assets/farm_assets.html"
    success_url = reverse_lazy('farm_crops')
    asset_base_url = reverse_lazy('farm_crops')
    form_class = get_generic_farm_asset_form(FarmCrop)
    datatable_fields = ['name', 'growth_stage' ,'parcel']


class FarmAnimalUpdateView(BaseFarmAssetUpdateView):
    model = FarmAnimal
    form_class = get_generic_farm_asset_form(FarmAnimal)
    template_name = 'farm_management/farm_assets/farm_assets.html'
    success_url = reverse_lazy('farm_animals')


class FarmAnimalListView(BaseFarmAssetListManagementView):
    model = FarmAnimal
    template_name = "farm_management/farm_assets/farm_assets.html"
    success_url = reverse_lazy('farm_animals')
    asset_base_url = reverse_lazy('farm_animals')
    form_class = get_generic_farm_asset_form(FarmAnimal)
    datatable_fields = ['name', 'species', 'parcel', ]


class AgriculturalMachineUpdateView(BaseFarmAssetUpdateView):
    model = AgriculturalMachine
    form_class = get_generic_farm_asset_form(AgriculturalMachine)
    template_name = 'farm_management/farm_assets/farm_assets.html'
    success_url = reverse_lazy('agri_machines')


class AgriculturalMachineListView(BaseFarmAssetListManagementView):
    model = AgriculturalMachine
    template_name = "farm_management/farm_assets/farm_assets.html"
    success_url = reverse_lazy('agri_machines')
    asset_base_url = reverse_lazy('agri_machines')
    form_class = get_generic_farm_asset_form(AgriculturalMachine)
    datatable_fields = ['name', 'model', 'parcel', ]