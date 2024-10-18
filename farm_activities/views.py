from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from .models import FarmCalendarActivity
from .forms import FarmCalendarActivityTypeForm, FarmCalendarActivityForm

class CalendarView(View):
    def get(self, request):
        return render(request, 'calendar.html')

class FarmCalendarActivityTypeCreateView(View):
    def get(self, request):
        form = FarmCalendarActivityTypeForm()
        return render(request, 'farm_activities/activities/activity_type_form.html', {'form': form})

    def post(self, request):
        form = FarmCalendarActivityTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('calendar')
        return render(request, 'farm_activities/activities/activity_type_form.html', {'form': form})

class FarmCalendarActivityCreateView(View):
    def get(self, request):
        form = FarmCalendarActivityForm()
        return render(request, 'farm_activities/activities/activity_form.html', {'form': form})

    def post(self, request):
        form = FarmCalendarActivityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('calendar')
        return render(request, 'farm_activities/activities/activity_form.html', {'form': form})


class FarmCalendarActivityListView(View):
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
