from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.generic import TemplateView

from farm_management.models import FarmParcel
from farm_management.forms.FarmParcelsForm import FarmParcelsForm


@method_decorator(never_cache, name='dispatch')
class FarmParcelView(TemplateView):
    template_name = "farm_parcels/farm_parcels.html"
    success_url = reverse_lazy('farm_parcels_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')

        if pk:
            farm_parcel = get_object_or_404(FarmParcel, pk=pk)
            form = FarmParcelsForm(instance=farm_parcel)
        else:
            farm_parcel = None
            form = FarmParcelsForm()

        context['form'] = form
        context['farm_parcel'] = farm_parcel
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')

        if pk:
            farm_parcel = get_object_or_404(FarmParcel, pk=pk)
            form = FarmParcelsForm(request.POST, instance=farm_parcel)
        else:
            farm_parcel = None
            form = FarmParcelsForm(request.POST)

        # Validate form and handle redirection or re-rendering with errors
        if form.is_valid():
            form.save()
            return redirect(self.success_url)

        context = self.get_context_data(**kwargs)
        context['form'] = form
        return render(request, self.template_name, context)

    # Handle DELETE requests for deleting
    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        farm_parcel = get_object_or_404(FarmParcel, pk=pk)
        farm_parcel.delete()
        return redirect(self.success_url)