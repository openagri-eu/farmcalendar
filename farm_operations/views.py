from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from .models import FarmOperation
from .forms import FarmOperationTypeForm, FarmOperationForm

class CalendarView(View):
    def get(self, request):
        return render(request, 'calendar.html')

class FarmOperationTypeCreateView(View):
    def get(self, request):
        form = FarmOperationTypeForm()
        return render(request, 'farm_operations/operations/operation_type_form.html', {'form': form})

    def post(self, request):
        form = FarmOperationTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('calendar')
        return render(request, 'farm_operations/operations/operation_type_form.html', {'form': form})

class FarmOperationCreateView(View):
    def get(self, request):
        form = FarmOperationForm()
        return render(request, 'farm_operations/operations/operation_form.html', {'form': form})

    def post(self, request):
        form = FarmOperationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('calendar')
        return render(request, 'farm_operations/operations/operation_form.html', {'form': form})


class FarmOperationListView(View):
    def get(self, request):
        operations_json_data = []
        for operation in FarmOperation.objects.select_related('operation_type').all():
            operations_json_data.append({
                'title': operation.title,
                'start': operation.start_time.isoformat(),
                'end': operation.end_time.isoformat(),
                'details': operation.details,
                'backgroundColor': operation.operation_type.background_color,
                'borderColor': operation.operation_type.border_color,
                'textColor': operation.operation_type.text_color,
                'details': operation.details,
            })
        return JsonResponse(operations_json_data, safe=False)
