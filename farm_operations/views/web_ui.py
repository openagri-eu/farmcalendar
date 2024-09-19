from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from ..models import FarmActivity
from ..forms import FarmActivityTypeForm, FarmActivityForm

class CalendarView(View):
    def get(self, request):
        return render(request, 'calendar.html')

class FarmActivityTypeCreateView(View):
    def get(self, request):
        form = FarmActivityTypeForm()
        return render(request, 'farmactivities/activities/activity_type_form.html', {'form': form})

    def post(self, request):
        form = FarmActivityTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('calendar')
        return render(request, 'farmactivities/activities/activity_type_form.html', {'form': form})

class FarmActivityCreateView(View):
    def get(self, request):
        form = FarmActivityForm()
        return render(request, 'farmactivities/activities/activity_form.html', {'form': form})

    def post(self, request):
        form = FarmActivityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('calendar')
        return render(request, 'farmactivities/activities/activity_form.html', {'form': form})


class FarmActivityListView(View):
    # in the future this view should be replaced by simply the rest API view
    # by changing in the calendar js how to parse the results into its required format
    def get(self, request):
        activities_json_data = []
        for activity in FarmActivity.objects.select_related('activity_type').all():
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
