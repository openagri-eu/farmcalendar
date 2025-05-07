from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from farm_calendar.utils.jwt_utils import get_token_from_jwt_request



class PrepareReportView(TemplateView, LoginRequiredMixin):
    template_name = "farm_management/reports/prepare_report.html"

    REPORT_TYPE = {
        'livestock': _('Livestock'),
        'irrigation': _('Irrigation'),
        'composting': _('Composting'),
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        readable_report_type = self.REPORT_TYPE[kwargs.get('report_type')]
        report_endpoint = settings.REPORTING_ENDPOINTS.get(kwargs.get('report_type'))
        report_result_base_endpoint = settings.REPORTING_ENDPOINTS.get('report_result_base')
        context['readable_report_type'] = readable_report_type
        context['report_endpoint'] = report_endpoint
        context['report_result_base_endpoint'] = report_result_base_endpoint
        token = get_token_from_jwt_request(self.request)
        context['access_token'] = token
        return context

