from django.urls import path
from django.contrib.auth.decorators import login_required


from .views import (
    CalendarView,
    FarmCalendarActivityCreateView, FarmCalendarActivityListView,
    FarmCalendarActivityTypeCreateView,
)



urlpatterns = [
    path('', login_required(CalendarView.as_view()), name='calendar'),
    path('create/', login_required(FarmCalendarActivityCreateView.as_view()), name='create_calendar_activity'),
    path('activities/', login_required(FarmCalendarActivityListView.as_view()), name='calendar_activity_list'),
    path('activity-type/create/', login_required(FarmCalendarActivityTypeCreateView.as_view()), name='create_activity_type'),
]