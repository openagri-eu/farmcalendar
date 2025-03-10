import os
import json
from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

import logging

from django.core.management.base import BaseCommand
from django.db import connections
from django.conf import settings



# Set up logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class Command(BaseCommand):
    help = "Output content for API.md with endpoints from Swagger's API schema."


    def parse_endpoints(self):
        if not os.path.exists(settings.API_SCHEMA_FILE_PATH):
            raise Exception(f'Missing API schema file used to register endpoints: {settings.API_SCHEMA_FILE_PATH}')

        schema = None
        with open(settings.API_SCHEMA_FILE_PATH, 'r') as file:
            schema = load(file, Loader=Loader)


        for path, methods in schema.get('paths', {}).items():
            if 'schema' in path:
                continue
            self.stdout.write(f'\n# Endpoint: {path}\n')
            for method, method_data in methods.items():
                method_str = method.upper()
                self.stdout.write(f'\n## {method_str}\n')
                operation_id_str = method_data.get('operationId', '').replace('_', ' ')
                self.stdout.write(f'Endpoint operation description: {operation_id_str.capitalize()}.')

                if 'parameters' in method_data:
                    self.stdout.write(f'\n### Parameters\n\n')
                    for param_data in method_data["parameters"]:
                        param = param_data['name']
                        schema_type = param_data['schema']['type']
                        param_desc = param_data.get('description', '').replace('\n', ' ')
                        if param == 'activity_type':
                            param_desc = 'ID of the farm calendar activity.'
                        if param == 'title':
                            param_desc = 'title of the farm calendar activity.'
                        if param == 'name':
                            param_desc = 'name of the asset.'
                        if param == 'responsible_agent':
                            param_desc = 'The responsible agent for this activity.'
                        if param == 'format':
                            param_desc = 'Forces a response format (i.e., Json or JsonLD).'
                        if param_desc == '':
                            param_desc = f'The {param.replace('_', ' ')}'
                        required_str = '[Required]' if param_data.get('required', False) else ''
                        param_str = f"**{param}**" if param_data.get('required', False) else f'{param}'
                        self.stdout.write(f' * {param_str} ({schema_type}){required_str}: {param_desc}.')


            self.stdout.write(f'\n## Example Response (GET/DELETE)\n\n')
            self.stdout.write((
                f'```json\n'
                f'\n```'
            ))
            self.stdout.write(f'\n## Example Request/Response (POST/PUT/PATCH)\n\n')
            self.stdout.write((
                f'```json\n'
                f'\n```'
            ))




    def handle(self, *args, **options):
        endpoints = self.parse_endpoints()
