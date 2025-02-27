from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView




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
        context['readable_report_type'] = readable_report_type
        return context

