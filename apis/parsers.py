from rest_framework.parsers import JSONParser
from rest_framework.exceptions import ParseError

from .renderers import JSONLDRenderer


class JSONLDParser(JSONParser):
    media_type = 'application/ld+json'
    renderer_class = JSONLDRenderer

    def parse(self, stream, media_type=None, parser_context=None):
        # Parse the incoming JSON-LD data
        data = super().parse(stream, media_type, parser_context)

        # Check if the data contains @graph (JSON-LD structure)
        if isinstance(data, dict) and "@graph" in data:
            # Extract data from the @graph field
            data = data["@graph"]

        # Handle the case where @graph might be a list of objects or a single object
        if isinstance(data, list):
            # Process each object inside the list (assuming they follow DRF model structure)
            return data
        else:
            # Single object
            return data
