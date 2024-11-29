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
        # if isinstance(data, dict) and 'results' in data:
        #     ocsm_context.append({
        #         "Pagination": "http://schema.org/DataFeed",
        #         "count": "http://schema.org/numberOfItems",
        #         "next": {
        #             "@id": "http://schema.org/nextItem",
        #             "@type": "@id"
        #         },
        #         "previous": {
        #             "@id": "http://schema.org/previousItem",
        #             "@type": "@id"
        #         },
        #     })
        #     context = {
        #         "@context": ocsm_context,
        #         "@graph": [
        #             {
        #                 "@type": "Pagination",
        #                 "count": data.get("count"),
        #                 "next": data.get("next"),
        #                 "previous": data.get("previous")
        #             }
        #         ] + data["results"]
        #     }

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