#!/usr/bin/env python
from uuid import uuid4
import os
import jwt
from datetime import datetime, timedelta
import json
import requests
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'farm_calendar.settings')

from django.conf import settings

payload = {
    # 'iat': 1722375999,
    'user_id': '1',
    'exp': datetime.utcnow() + timedelta(days=1),
    'token_type': 'access',
    'jti': str(uuid4()),
}

token = jwt.encode(payload, settings.JWT_SIGNING_KEY, algorithm=settings.JWT_ALG)


# url = 'http://localhost:8002/api/v1/Farm/1/'
url = 'http://localhost:8002/api/v1/FarmParcels/2/'
# url = 'http://localhost:8002/api/v1/FertilizationOperation/1/'

jwt_token = token

headers = {
    'Authorization': f'Bearer {jwt_token}',
    'Accept': 'application/ld+json',  # Requesting JSON-LD format
}

cookies = {settings.JWT_COOKIE_NAME: jwt_token}

request_kwargs = {
}
use_get_parameter = False
if not use_get_parameter:

    use_headers = True
    if use_headers:
        request_kwargs['headers'] = headers
    else:
        request_kwargs['cookies'] = cookies
else:
    request_kwargs['params'] = {
        'auth_token': token
    }

response = requests.get(url, **request_kwargs)

print(f"Response Status Code: {response.status_code}\n\n")
print(f"Response Content: {response.text}\n\n")
print(f"Response Content: {json.dumps(response.json(), indent=4)}\n\n")
print(f"Response Headers: {response.headers}\n\n")  # Print headers to check Content-Type

# Check if the Content-Type is application/ld+json
if response.headers.get('Content-Type') == 'application/ld+json':
    print("Response is in JSON-LD format.")
else:
    print("Response is NOT in JSON-LD format.")