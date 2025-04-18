import json

from django.contrib import messages
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.db import DatabaseError, IntegrityError
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from farm_management.models import Farm
from farm_management.forms import FarmForm

from farm_management.constants import *


@method_decorator(never_cache, name='dispatch')
class FarmView(LoginRequiredMixin, TemplateView):
    template_name = "farm_management/farm_master.html"
    success_url = reverse_lazy('farms')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        farms = Farm.active_objects.all()

        # Custom serialization to include related fields
        farms_data = []
        for farm in farms:
            # `active_address` is now a single object or None if no active address exists
            address = getattr(farm, 'active_address', None)

            farm_data = {
                "model": "farm_management.farmmaster",
                "pk": str(farm.pk),
                "fields": {
                    "name": farm.name,
                    "description": farm.description,
                    "administrator": farm.administrator,
                    "contact_person_firstname": farm.contact_person_firstname,
                    "contact_person_lastname": farm.contact_person_lastname,
                    "telephone": farm.telephone,
                    "vat_id": farm.vat_id,
                    "status": farm.status,
                    "created_at": farm.created_at.isoformat(),
                    "updated_at": farm.updated_at.isoformat(),
                    "admin_unit_l1": farm.admin_unit_l1,
                    "admin_unit_l2": farm.admin_unit_l2,
                    "address_area": farm.address_area,
                    "municipality": farm.municipality,
                    "community": farm.community,
                    "locator_name": farm.locator_name,
                }
            }
            farms_data.append(farm_data)

        context["farms"] = json.dumps(farms_data)
        return context

    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        # Determine if editing or creating a new Farm
        if pk:
            farm = get_object_or_404(Farm, pk=pk)
            # Pre-fill the form with the farm data and related address data if available
            initial_data = {
                'admin_unit_l1': farm.admin_unit_l1,
                'admin_unit_l2': farm.admin_unit_l2,
                'address_area': farm.address_area,
                'municipality': farm.municipality,
                'community': farm.community,
                'locator_name': farm.locator_name,
            }
            form = FarmForm(instance=farm, initial=initial_data)
        else:
            # Creating a new Farm
            form = FarmForm()

        context = self.get_context_data(**kwargs)
        context.update({
            'form': form,
            'is_edit': bool(pk)
        })
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        org_farm_name = None
        try:
            if pk:
                # Update an existing Farm
                farm = get_object_or_404(Farm, pk=pk)
                org_farm_name = farm.name
                form = FarmForm(request.POST, instance=farm)
            else:
                # Create a new Farm
                form = FarmForm(request.POST)

            if form.is_valid():
                # Save the Farm
                farm_instance = form.save(commit=False)

                if pk:
                    farm_instance.lang_code = org_farm_name

                farm_instance.save()

                # # Save the FarmAddress
                # farm_address, _ = FarmAddress.objects.get_or_create(farm=farm_instance)
                # farm_address.admin_unit_l1 = form.cleaned_data.get('admin_unit_l1')
                # farm_address.admin_unit_l2 = form.cleaned_data.get('admin_unit_l2')
                # farm_address.address_area = form.cleaned_data.get('address_area')
                # farm_address.municipality = form.cleaned_data.get('municipality')
                # farm_address.community = form.cleaned_data.get('community')
                # farm_address.locator_name = form.cleaned_data.get('locator_name')
                # farm_address.save()

                messages.success(request, "Farm saved successfully.")
                return redirect(self.success_url)
            else:
                messages.error(request, ERROR_PROCESSING)
                context = self.get_context_data(**kwargs)
                context['form'] = form
                context['is_edit'] = bool(pk)
                return render(request, self.template_name, context)
        except ValidationError as e:
            # Handle validation errors
            error_message = f"Validation Error: {str(e)}"
            return render(request, self.template_name, {'error': error_message})

        except (IntegrityError, DatabaseError) as e:
            # Handle database errors
            error_message = f"Database Error: {str(e)}"
            return render(request, self.template_name, {'error': error_message})

        except Exception as e:
            # Catch-all for any other exceptions
            error_message = f"An unexpected error occurred: {str(e)}"
            return render(request, self.template_name, {'error': error_message})

    def delete(self, request, *args, **kwargs):
        # Handle DELETE requests to delete a Farm
        pk = kwargs.get('pk')
        try:
            farm = get_object_or_404(Farm, pk=pk)
            farm.delete()
            return redirect(self.success_url)

        except ObjectDoesNotExist as e:
            # Handle case where the Farm does not exist
            error_message = f"Error: {str(e)}"
            return render(request, self.template_name, {'error': error_message})

        except (IntegrityError, DatabaseError) as e:
            # Handle database errors
            error_message = f"Database Error: {str(e)}"
            return render(request, self.template_name, {'error': error_message})

        except Exception as e:
            # Catch-all for any other exceptions
            error_message = f"An unexpected error occurred: {str(e)}"
            return render(request, self.template_name, {'error': error_message})
