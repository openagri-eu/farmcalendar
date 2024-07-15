#!/usr/bin/env python

import os
import jwt
from datetime import datetime, timedelta
import requests
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'farm_calendar.settings')
payload = {
    'user_id': "admin@admin.com",
    'exp': datetime.utcnow() + timedelta(days=1)
}

token = jwt.encode(payload, settings.JWT_SIGNING_KEY, algorithm=settings.JWT_ALG)

# print(">>>>")
# print(token)  # Print token as string
# print(">>>>")


# url = 'http://localhost:8000/'
url = 'http://localhost:8000/api/FarmPlants/'

jwt_token = token

headers = {
    'Authorization': f'Bearer {jwt_token}',
}

response = requests.get(url, headers=headers)
# import ipdb; ipdb.set_trace()

print(f"Response Status Code: {response.status_code}")
print(f"Response Content: {response.text}")

