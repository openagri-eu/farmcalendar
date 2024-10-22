from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.generic import TemplateView


@method_decorator(never_cache, name='dispatch')
class FarmParcelView(TemplateView):
    template_name = "farm_parcels/farm_parcels.html"


