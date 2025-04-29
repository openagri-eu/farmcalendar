from django.urls import path
from django.contrib.auth.decorators import login_required


from .views import (
    CalendarView,
    FarmCalendarActivityTypeListView,
    FarmCalendarActivityTypeCreateView,
    FarmCalendarActivityTypeEditView,
    FarmCalendarActivityCreateByTypeView,
    FarmCalendarActivityListView,
    FarmCalendarActivityEdit,
    PreRegisterCalendarActivityView,
    FarmCalendarActivityAutocomplete,
)



urlpatterns = [
    path('', CalendarView.as_view(), name='calendar'),
    path('register-activity/select-type', PreRegisterCalendarActivityView.as_view(), name='pre_register_calendar_activity'),
    path('register-activity/<str:activity_type>', FarmCalendarActivityCreateByTypeView.as_view(), name='create_calendar_activity'),
    path('activities/', FarmCalendarActivityListView.as_view(), name='calendar_activity_list'),
    path('activities/<uuid:pk>/', FarmCalendarActivityEdit.as_view(), name='calendar_activity_edit'),
    path('activity-type/create/', FarmCalendarActivityTypeCreateView.as_view(), name='create_activity_type'),
    path('activity-types/', FarmCalendarActivityTypeListView.as_view(), name='list_activity_type'),
    path('activity-types/<uuid:pk>/', FarmCalendarActivityTypeEditView.as_view(), name='edit_activity_type'),
    path('activities-autocomplete/', FarmCalendarActivityAutocomplete.as_view(), name='activities-autocomplete'),
]
