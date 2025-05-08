from urllib.parse import urljoin
from django.conf import settings

import requests


class AgstackClient:
    """
    A simple client for interacting with the AgStack API.
    """

    def __init__(self):
        self.api_url = settings.AGSTACK_ASSET_REGISTY_API_URL

    def register_field_boundary(self, wkt_geometry, threshold=95, s2_index=(8, 13)):
        s2_index_str = ",".join(map(str, s2_index))

        headers = {
            "API-KEYS-AUTHENTICATION": "true",
            "API-KEY": settings.AGSTACK_API_KEY,
            "CLIENT-SECRET": settings.AGSTACK_CLIENT_SECRET,
            # # (Optional)
            # "AUTOMATED-FIELD": "1"
        }

        data = {
            "wkt": wkt_geometry,
            # "threshold": threshold,  # Optional, defaults to 95 if not provided
            # "s2_index": s2_index_str  # Optional: comma-separated S2 indices if needed
        }
        endpoint_url = urljoin(self.api_url, settings.AGSTACK_ENDPOINTS['register_field_boundary'])
        resp = requests.post(endpoint_url, json=data, headers=headers)

        geo_id = None
        try:
            result = resp.json()
            if 'Geo Id' in result:
                geo_id = result['Geo Id']
            elif 'matched geo ids' in result:
                geo_id = result['matched geo ids'][0]
            else:
                raise ValueError("Invalid response from AgStack API")
        except Exception as e:
            raise ValueError("Invalid response from AgStack API")
        return geo_id


if __name__ == '__main__':

    client = AgstackClient()

    wkt_geometry = "POLYGON((5.714800882907841 50.83967331197391,5.714729694830028 50.839206943235155,5.716022320453463 50.839169065366434,5.715939892152838 50.83967094463168,5.714800882907841 50.83967331197391))"
    print(client.register_field_boundary(wkt_geometry))

