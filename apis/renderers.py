from django.conf import settings

from rest_framework.renderers import JSONRenderer



class JSONLDRenderer(JSONRenderer):
    media_type = 'application/ld+json'
    format = 'jsonld'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        request = renderer_context.get('request', None)
        if request and request.method == 'OPTIONS':
            # If it's an OPTIONS request, do not return JSON-LD
            return super().render(data, accepted_media_type, renderer_context)

        ocsm_context = settings.OCSM_JSONLD_CONTEXT['@context'].copy()

        # should handle paginated responses differently?
        # Check if we are dealing with a paginated response
        if isinstance(data, dict) and 'results' in data:
            # Handle pagination and results separately
            context = {
                "count": data.get("count"),
                "next": data.get("next"),
                "previous": data.get("previous"),
                "results": [
                    {
                        "@context": ocsm_context,
                        "@graph": data["results"]
                    }
                ]
            }

        # Check if data is a list for @graph
        elif isinstance(data, list):
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