from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from .models import Activity, ActivityType
from .forms import ActivityTypeForm, ActivityForm

class CalendarView(View):
    def get(self, request):
        return render(request, 'calendar.html')

class ActivityTypeCreateView(View):
    def get(self, request):
        form = ActivityTypeForm()
        return render(request, 'farmactivities/activities/activity_type_form.html', {'form': form})

    def post(self, request):
        form = ActivityTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('calendar')
        return render(request, 'farmactivities/activities/activity_type_form.html', {'form': form})

class ActivityCreateView(View):
    def get(self, request):
        form = ActivityForm()
        return render(request, 'farmactivities/activities/activity_form.html', {'form': form})

    def post(self, request):
        form = ActivityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('calendar')
        return render(request, 'farmactivities/activities/activity_form.html', {'form': form})


class ActivityListView(View):
    def get(self, request):
        activities_json_data = []
        for activity in Activity.objects.select_related('activity_type').all():
            activities_json_data.append({
                'title': activity.title,
                'start': activity.start_time.isoformat(),
                'end': activity.end_time.isoformat(),
                'details': activity.details,
                'backgroundColor': activity.activity_type.background_color,
                'borderColor': activity.activity_type.border_color,
                'textColor': activity.activity_type.text_color,
                'details': activity.details,
            })
        return JsonResponse(activities_json_data, safe=False)
