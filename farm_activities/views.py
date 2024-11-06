from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

from .models import (
    FarmCalendarActivity,
    FarmCalendarActivityType,
)
from .forms import (
    FarmCalendarActivityTypeSelectionForm,
    FarmCalendarActivityTypeForm,
    FarmCalendarActivityForm,
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
        form = GenericActivityForm(initial={'activity_type': activity_type_instance})
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
            })
        return JsonResponse(activities_json_data, safe=False)
