from rest_framework.renderers import JSONRenderer

class JSONLDRenderer(JSONRenderer):
    media_type = 'application/ld+json'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        # Check if data is a list for @graph
        if isinstance(data, list):
            context = {
                "@context": "https://schema.org",
                "@graph": data  # Use the serialized items directly
            }
        else:
            context = {
                "@context": "https://schema.org",
                "@graph": [data]  # Wrap single item in a list
            }
        return super().render(context, accepted_media_type, renderer_context)