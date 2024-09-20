from django.urls import path
from django.contrib.auth.decorators import login_required


from .views import (
    CalendarView,
    FarmOperationCreateView, FarmOperationListView,
    FarmOperationTypeCreateView,
)



urlpatterns = [
    path('', login_required(CalendarView.as_view()), name='calendar'),
    path('create/', FarmOperationCreateView.as_view(), name='create_operation'),
    path('operations/', login_required(FarmOperationListView.as_view()), name='operation_list'),
    path('operation-type/create/', FarmOperationTypeCreateView.as_view(), name='create_operation_type'),
]