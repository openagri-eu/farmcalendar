from django.urls import path
from .views import (
    CalendarView,
    ActivityCreateView, ActivityListView,
    ActivityTypeCreateView,
)

urlpatterns = [
    path('', CalendarView.as_view(), name='calendar'),
    path('create/', ActivityCreateView.as_view(), name='create_activity'),
    path('activities/', ActivityListView.as_view(), name='activity_list'),
    path('activity-type/create/', ActivityTypeCreateView.as_view(), name='create_activity_type'),
]