import json

from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder
from django.db import DatabaseError, IntegrityError
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.generic import TemplateView

from farm_management.models import FarmMaster, FarmAddress
from farm_management.forms.FarmMasterForm import FarmMasterForm


@method_decorator(never_cache, name='dispatch')
class FarmMasterView(TemplateView):
    template_name = "farm_management/farm_master.html"
    success_url = reverse_lazy('farm_master_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        farms = FarmMaster.active_objects.select_related('address').all()

        # Custom serialization to include related fields
        farms_data = [
            {
                "model": "farm_management.farmmaster",
                "pk": farm.pk,
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
                    # Include related address fields if they exist
                    "admin_unit_l1": farm.address.admin_unit_l1 if farm.address else None,
                    "admin_unit_l2": farm.address.admin_unit_l2 if farm.address else None,
                    "address_area": farm.address.address_area if farm.address else None,
                    "municipality": farm.address.municipality if farm.address else None,
                    "community": farm.address.community if farm.address else None,
                    "locator_name": farm.address.locator_name if farm.address else None,
                }
            }
            for farm in farms
        ]

        context["farms"] = json.dumps(farms_data)
        return context

    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')

        # Determine if editing or creating a new Farm
        if pk:
            farm = get_object_or_404(FarmMaster, pk=pk)
            # Pre-fill the form with the farm data and related address data if available
            initial_data = {}
            if hasattr(farm, 'address'):
                initial_data = {
                    'admin_unit_l1': farm.address.admin_unit_l1,
                    'admin_unit_l2': farm.address.admin_unit_l2,
                    'address_area': farm.address.address_area,
                    'municipality': farm.address.municipality,
                    'community': farm.address.community,
                    'locator_name': farm.address.locator_name,
                }
            form = FarmMasterForm(instance=farm, initial=initial_data)
        else:
            # Creating a new Farm
            form = FarmMasterForm()

        context = self.get_context_data(**kwargs)
        context.update({
            'form': form,
            'is_edit': bool(pk)
        })
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        try:
            if pk:
                # Update an existing Farm
                farm = get_object_or_404(FarmMaster, pk=pk)
                form = FarmMasterForm(request.POST, instance=farm)
            else:
                # Create a new Farm
                form = FarmMasterForm(request.POST)

            if form.is_valid():
                # Save the Farm
                farm = form.save(commit=True)

                # Save the FarmAddress
                farm_address, _ = FarmAddress.objects.get_or_create(farm=farm)
                farm_address.admin_unit_l1 = form.cleaned_data.get('admin_unit_l1')
                farm_address.admin_unit_l2 = form.cleaned_data.get('admin_unit_l2')
                farm_address.address_area = form.cleaned_data.get('address_area')
                farm_address.municipality = form.cleaned_data.get('municipality')
                farm_address.community = form.cleaned_data.get('community')
                farm_address.locator_name = form.cleaned_data.get('locator_name')
                farm_address.save()

                # Redirect for standard requests
                return redirect(self.success_url)

            # If form is not valid, re-render with errors
            context = self.get_context_data(**kwargs)
            context['form'] = form

            # Render the form with errors for standard requests
            return render(request, self.template_name, context)
        except ObjectDoesNotExist as e:
            # Handle cases where the Farm or FarmAddress does not exist
            error_message = f"Error: {str(e)}"
            return render(request, self.template_name, {'error': error_message})
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
            farm = get_object_or_404(FarmMaster, pk=pk)
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
