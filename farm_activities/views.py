from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import CharField
from django.db.models.functions import Concat
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views import View

from .models import (
    FarmCalendarActivity,
    FarmCalendarActivityType,
)
from .forms import (
    FarmCalendarActivityTypeSelectionForm,
    FarmCalendarActivityTypeForm,
    get_generic_farm_calendar_activity_form,
)

class CalendarView(LoginRequiredMixin, View):
    template_name = 'calendar.html'
    def get(self, request):
        return render(request, self.template_name)


class FarmCalendarActivityTypeCreateView(LoginRequiredMixin, View):
    def get(self, request):
        form = FarmCalendarActivityTypeForm()
        return render(request, 'farm_activities/activities/activity_type_form.html', {'form': form})

    def post(self, request):
        form = FarmCalendarActivityTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('calendar')
        return render(request, 'farm_activities/activities/activity_type_form.html', {'form': form})


class PreRegisterCalendarActivityView(LoginRequiredMixin, View):
    template_name = 'farm_activities/activities/pre_activity_form.html'
    def get(self, request):
        form = FarmCalendarActivityTypeSelectionForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = FarmCalendarActivityTypeSelectionForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            return redirect('create_calendar_activity', activity_type=cleaned_data['activity_type'].name)
        return render(request, self.template_name, {'form': form})


class FarmCalendarActivityCreateByTypeView(LoginRequiredMixin, View):
    template_name = 'farm_activities/activities/activity_form.html'

    def get(self, request, activity_type):
        GenericActivityForm = get_generic_farm_calendar_activity_form(activity_type=activity_type)
        if GenericActivityForm is None:
            redirect('pre_register_calendar_activity')
        activity_type_instance = FarmCalendarActivityType.objects.get(name=activity_type)
        form = GenericActivityForm(initial={'activity_type': activity_type_instance, 'title': activity_type_instance.name})
        return render(request, self.template_name, {'form': form})

    def post(self, request, activity_type):
        GenericActivityForm = get_generic_farm_calendar_activity_form(activity_type=activity_type)
        form = GenericActivityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('calendar')
        return render(request, self.template_name, {'form': form})


class FarmCalendarActivityListView(LoginRequiredMixin, View):
    def get(self, request):
        activities_json_data = []
        for activity in FarmCalendarActivity.objects.select_related('activity_type').all():
            end_time = activity.end_datetime.isoformat() if activity.end_datetime else None
            activities_json_data.append({
                'title': activity.title,
                'start': activity.start_datetime.isoformat(),
                'end': end_time,
                'details': activity.details,
                'backgroundColor': activity.activity_type.background_color,
                'borderColor': activity.activity_type.border_color,
                'textColor': activity.activity_type.text_color,
                'detail_url': reverse('calendar_activity_edit', kwargs={'pk': activity.pk})
            })
        return JsonResponse(activities_json_data, safe=False)


class FarmCalendarActivityEdit(LoginRequiredMixin, View):
    template_name = 'farm_activities/activities/activity_form.html'

    def get_specific_activity_object_and_form(self, pk):
        base_object = get_object_or_404(FarmCalendarActivity, pk=pk)
        GenericActivityForm = get_generic_farm_calendar_activity_form(activity_type=base_object.activity_type.name)
        main_object = get_object_or_404(GenericActivityForm.Meta.model.objects.prefetch_related('activity_type', 'nested_activities'), pk=pk)
        return main_object, GenericActivityForm

    def get_asset_delete_api_url(self, model_name, pk):
        asset_base_api_url = reverse_lazy(
            f'{model_name}-detail',
            kwargs={'version': settings.SHORT_API_VERSION, 'pk':pk}
        )
        return asset_base_api_url

    def get(self, request, pk):
        main_object, GenericActivityForm = self.get_specific_activity_object_and_form(pk)
        form = GenericActivityForm(instance=main_object)
        delete_url = self.get_asset_delete_api_url(main_object._meta.model_name, pk)
        context = {
            'form': form,
            'is_edit': True,
            'delete_url': delete_url
        }
        return render(request, self.template_name, context=context)

    def post(self, request, pk):
        main_object, GenericActivityForm = self.get_specific_activity_object_and_form(pk)
        form = GenericActivityForm(request.POST, instance=main_object)
        if form.is_valid():
            form.save()
            return redirect('calendar')
        delete_url = self.get_asset_delete_api_url(main_object.Meta.model_name, pk)
        context = {
            'form': form,
            'is_edit': True,
            'delete_url': delete_url
        }
        return render(request, self.template_name, context=context)


class FarmCalendarActivityAutocomplete(View):
    def get(self, request, *args, **kwargs):
        search_term = request.GET.get('term', '')

        if search_term:

            search_parts = search_term.split()

            # Annotate by concatenating the title and start_datetime
            annotated_qs = FarmCalendarActivity.objects.annotate(
                activity_str=Concat('title', 'start_datetime', output_field=CharField())
            )

            filtered_qs = None
            for part in search_parts:
                if filtered_qs is None:
                    filtered_qs = annotated_qs.filter(activity_str__icontains=part)
                else:
                    filtered_qs = filtered_qs.filter(activity_str__icontains=part)


            qs_values = filtered_qs.values('pk', 'title', 'start_datetime')
            objs = [
                {
                    'pk': activity['pk'],
                    'activity': str(FarmCalendarActivity(**activity))
                }
                for activity in qs_values
            ]

            return JsonResponse(objs, safe=False)

        return JsonResponse([], safe=False)