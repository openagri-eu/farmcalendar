import os
from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

import logging

from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.db import connections
from django.db.migrations.executor import MigrationExecutor
from django.db.migrations.recorder import MigrationRecorder
from django.conf import settings

import requests

from farm_activities.models import FarmCalendarActivityType

# Set up logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class Command(BaseCommand):
    help = "Register all endpoints for Swagger's API schema into gatekeeper, if gatekeeper is present"

    def login_to_gatekeeper(self):
        data = {
            "username": f"{settings.FARMCALENDAR_GATEKEEPER_USER}",
            "password": f"{settings.FARMCALENDAR_GATEKEEPER_PASSWORD}"
        }
        response = requests.post(settings.GATEKEEPER_API_LOGIN_URL, data=data)
        if response.status_code != 200:
            raise Exception(
                (
                 f'[Status Code {response.status_code}] '
                 f'Could not logging into gatekeeper "{settings.GATEKEEPER_API_LOGIN_URL}" '
                 f'with the provided username and password from "'
                 f'FARMCALENDAR_GATEKEEPER_USER and FARMCALENDAR_GATEKEEPER_PASSWORD."'
                )
            )
        resp_data = response.json()
        token = resp_data.get('access')
        return token

    def register_endpoints(self, endpoints):
        total_endpoints = len(endpoints)
        logger.info(f'Registering {total_endpoints} endpoints ...')

        failed_endpoints_reg = {}
        for endpoint_data in endpoints:
            endpoint = endpoint_data['endpoint']
            logger.debug(f'Will try to register endpoint with data: {endpoint_data}')
            req_headers = {'Authorization': f'Bearer {self.token}'}
            response = requests.post(settings.GATEKEEPER_ENDPOINT_REG_URL, json=endpoint_data, headers=req_headers)
            if response.status_code in [200, 201]:
                logger.info(f'Successfully registered endpoint: {endpoint}')
            else:
                logger.error(f'Failed to register endpoint: {endpoint}')
                failed_endpoints_reg[endpoint] = endpoint_data
        if len(failed_endpoints_reg) > 0:
            raise Exception(f'Failed to register {len(failed_endpoints_reg.keys())} endpoints: {list(failed_endpoints_reg.keys())}')


    def extract_params(self, method_data):
        params = []
        if 'parameters' in method_data:
            for param in method_data['parameters']:
                param_name = param['name']
                param_in_query = param.get('in','') == 'query'
                param_type = param['schema']['type']
                if param_in_query:
                    params.append(f"{param_name}={{{param_type}}}")
        return params

    def parse_endpoints(self):
        if not os.path.exists(settings.API_SCHEMA_FILE_PATH):
            raise Exception(f'Missing API schema file used to register endpoints: {settings.API_SCHEMA_FILE_PATH}')

        schema = None
        with open(settings.API_SCHEMA_FILE_PATH, 'r') as file:
            schema = load(file, Loader=Loader)

        endpoint_data = []

        for path, methods in schema.get('paths', {}).items():
            all_methods = [k.upper() for k in methods.keys()]
            all_methods.extend(['HEAD', 'OPTIONS'])
            combined_params = set()

            for method, method_data in methods.items():
                combined_params.update(self.extract_params(method_data))

            data = {
                "base_url": settings.INTERNAL_SERVICE_URL,
                "service_name": settings.INTERNAL_SERVICE_NAME,
                "endpoint": path,
                "methods": all_methods,
                "version": settings.SHORT_API_VERSION,
            }
            if len(combined_params) > 0:
                data['params'] = "&".join(combined_params)

            endpoint_data.append(data)

        return endpoint_data

    def handle(self, *args, **options):
        logger.info('Checking if using GATEKEEPER...')
        if settings.GATEKEEPER_ENDPOINT_REG_URL is None:
            logger.info('No GATEKEEPER_ENDPOINT_REG_URL defined. Ignoring service endpoint registration...')
            return

        self.token = self.login_to_gatekeeper()
        endpoints = self.parse_endpoints()

        self.register_endpoints(endpoints)

        logger.info('Finished registering endpoints.')