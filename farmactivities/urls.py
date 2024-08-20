from django.urls import path, include
from django.contrib.auth.decorators import login_required

from rest_framework import routers

from .views import (
    CalendarView,
    ActivityCreateView, ActivityListView,
    ActivityTypeCreateView,
    ActivityViewSet,
    ActivityTypeViewSet,
)



# router = routers.DefaultRouter()
# router.register(r'FarmActivities', ActivityViewSet)
# router.register(r'FarmActivityTypes', ActivityTypeViewSet)



urlpatterns = [
    path('', login_required(CalendarView.as_view()), name='calendar'),
    path('create/', ActivityCreateView.as_view(), name='create_activity'),
    path('activities/', login_required(ActivityListView.as_view()), name='activity_list'),
    path('activity-type/create/', ActivityTypeCreateView.as_view(), name='create_activity_type'),
    # path('api/', include(router.urls)),
]