from django.urls import path
from django.contrib.auth.decorators import login_required


from .views import (
    CalendarView,
    FarmCalendarActivityCreateByTypeView, FarmCalendarActivityListView,
    FarmCalendarActivityTypeCreateView,
    PreRegisterCalendarActivityView
)



urlpatterns = [
    path('', CalendarView.as_view(), name='calendar'),
    path('register-activity/select-type', PreRegisterCalendarActivityView.as_view(), name='pre_register_calendar_activity'),
    path('register-activity/<str:activity_type>', FarmCalendarActivityCreateByTypeView.as_view(), name='create_calendar_activity'),
    path('activities/', FarmCalendarActivityListView.as_view(), name='calendar_activity_list'),
    path('activity-type/create/', FarmCalendarActivityTypeCreateView.as_view(), name='create_activity_type'),
]