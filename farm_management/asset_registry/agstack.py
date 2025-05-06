import hashlib
import hmac
import urllib.parse

import requests

from django.conf import settings

class AgstackClient:
    """
    A simple client for interacting with the AgStack API.
    """

    def __init__(self):
        self.api_url = settings.AGSTACK_API_URL


    def get_or_create_asset_for_field(self, wkt_geometry):
        """
        Get or create an asset in AgStack for the given WKT geometry.
        """
        endpoint = settings.AGSTACK_ENDPOINTS['get_or_create_asset_for_field']

        data = {
            'bound': wkt_geometry,
            'create': 1,
            'access_key': settings.AGSTACK_ACCESS_KEY,
        }
        signature = self._generate_signature(data)
        data.update({
            'signature': signature,
        })
        req = requests.get(endpoint, params=data)
        if req.status_code == 200:
            # {
            #     "geoid": "string",
            #     "domain": "test.com",
            #     "intersection": 0.5,
            #     "inclusion": 0.9,
            #     "overlap": 0.7,
            #     "resolution_level": 13
            # }
            response = req.json()
            if response.get('geoid'):
                return response
            else:
                raise ValueError("Invalid response from AgStack API")
        else:
            raise ValueError(f"Error {req.status_code}: {req.text}")
    def _generate_signature(self, data):
        """
        Generate a signature for the given data using the AgStack API secret key.
        """

        sorted_params = sorted(params.items())
        query_string = urllib.parse.urlencode(sorted_params)

        # Step 2: Generate HMAC-SHA256 signature
        signature = hmac.new(client_secret, query_string.encode('utf-8'), hashlib.sha256).hexdigest()
