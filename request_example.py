#!/usr/bin/env python
from uuid import uuid4
import os
import jwt
from datetime import datetime, timedelta
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

# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJleHAiOjE3MjIzNjc4MjcsImlhdCI6MTcyMjM2NDIyN30.c-BHVCmclu7wZBo875wTwl3gIchTvVbGYA6P5M-BfWA
# token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJleHAiOjE3MjIzNjgyMTgsImlhdCI6MTcyMjM2NDYxOH0.xNx4a_ZgOYLFE3beGDdrie25ovhtA8W_oC2eQTdqFYs"

# token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJleHAiOjE3MjIzNzk1OTksImlhdCI6MTcyMjM3NTk5OX0.-TAxCkEfDryLrdjG1pSpEALjrcqsWDt8i1-DjreMwbw"
# url = 'http://localhost:8000/'
# url = 'http://localhost:8002/test_perm'
# url = 'http://localhost:8002/api/FarmPlants/'
# url = 'http://localhost:8000/api/resources/FarmPlants/'
# url = 'http://localhost:8000/api/resources/FarmPlants/'
url = 'http://localhost:8000/api/resources/WeeklyWeatherForecast/'

# url = 'http://localhost:8002/post_auth'

jwt_token = token

headers = {
    'Authorization': f'Bearer {jwt_token}',
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

print(f"Response Status Code: {response.status_code}")
print(f"Response Content: {response.text}")

