from django.conf import settings

from rest_framework.renderers import JSONRenderer



class JSONLDRenderer(JSONRenderer):
    media_type = 'application/ld+json'
    format = 'jsonld'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        ocsm_context = settings.OCSM_JSONLD_CONTEXT['@context'].copy()
        # Check if data is a list for @graph
        if isinstance(data, list):
            context = {
                "@context": ocsm_context,
                "@graph": data  # Use the serialized items directly
            }
        else:
            context = {
                "@context": ocsm_context,
                "@graph": [data]  # Wrap single item in a list
            }
        return super().render(context, accepted_media_type, renderer_context)