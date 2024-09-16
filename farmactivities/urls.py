from django.urls import path
from django.contrib.auth.decorators import login_required


from .views import (
    CalendarView,
    FarmActivityCreateView, FarmActivityListView,
    FarmActivityTypeCreateView,
)



urlpatterns = [
    path('', login_required(CalendarView.as_view()), name='calendar'),
    path('create/', FarmActivityCreateView.as_view(), name='create_activity'),
    path('activities/', login_required(FarmActivityListView.as_view()), name='activity_list'),
    path('activity-type/create/', FarmActivityTypeCreateView.as_view(), name='create_activity_type'),
]