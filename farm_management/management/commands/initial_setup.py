import json
import os
import logging

from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.db import connections
from django.db.migrations.executor import MigrationExecutor
from django.db.migrations.recorder import MigrationRecorder

from django.conf import settings

from farm_activities.models import FarmCalendarActivityType
from farm_management.models.base import AdminMenuMaster

# Set up logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class Command(BaseCommand):
    help = "Initial setup command, based on the same one in gatekeeper's command"

    # Check if there is any existing data for AdminMenuMaster or FarmCalendarActivityType
    def check_for_initial_data(self):
        return not FarmCalendarActivityType.objects.exists() or not AdminMenuMaster.objects.exists()

    # Load initial data from JSON file
    def load_initial_data_from_file(self):
        json_file_path = os.path.join(os.path.dirname(__file__), 'config', 'initial_admin_menu_data.json')
        if not os.path.exists(json_file_path):
            self.stdout.write(self.style.ERROR(f'Initial data file {json_file_path} not found.'))
            logger.error(f'Initial data file {json_file_path} not found.')
            return None

        try:
            with open(json_file_path, 'r') as json_file:
                return json.load(json_file)
        except json.JSONDecodeError as e:
            self.stdout.write(self.style.ERROR(f'Error decoding JSON: {e}'))
            logger.error(f'Error decoding JSON: {e}')
            return None

    def setup_initial_data(self):
        # Populate FarmCalendarActivityType
        self.stdout.write(self.style.SUCCESS('Setting up FarmCalendarActivityType data...'))
        for def_operation_type in settings.DEFAULT_CALENDAR_ACTIVITY_TYPES.values():
            operation = FarmCalendarActivityType(**def_operation_type)
            operation.save()

        # Load initial data for AdminMenuMaster from the JSON file
        initial_admin_menu_data = self.load_initial_data_from_file()
        if initial_admin_menu_data is None:
            self.stdout.write(self.style.ERROR('Failed to load initial AdminMenuMaster data.'))
            return

        # Populate AdminMenuMaster using the loaded data with batch insertion for better performance
        self.stdout.write(self.style.SUCCESS('Setting up AdminMenuMaster data...'))
        new_entries = [
            AdminMenuMaster(**menu_data)
            for menu_data in initial_admin_menu_data
            if not AdminMenuMaster.objects.filter(menu_name=menu_data['menu_name']).exists()
        ]
        try:
            AdminMenuMaster.objects.bulk_create(new_entries, ignore_conflicts=True)
            self.stdout.write(self.style.SUCCESS(f'Successfully added {len(new_entries)} AdminMenuMaster entries.'))
            logger.info(f'Successfully added {len(new_entries)} AdminMenuMaster entries.')
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Failed to create AdminMenuMaster entries. Error: {e}'))
            logger.error(f'Failed to create AdminMenuMaster entries. Error: {e}')

    # Check for pending migrations
    def check_pending_migrations(self):
        for connection in connections.all():
            executor = MigrationExecutor(connection)
            targets = executor.loader.graph.leaf_nodes()
            recorder = MigrationRecorder(connection)
            applied = recorder.applied_migrations()

            unapplied = [migration for migration in targets if migration not in applied]

            if unapplied:
                self.stdout.write(self.style.SUCCESS(f'Pending migrations detected: {unapplied}'))
                logger.info(f'Pending migrations detected: {unapplied}')
                return True
        self.stdout.write(self.style.SUCCESS('No pending migrations detected.'))
        logger.info('No pending migrations detected.')
        return False

    def handle(self, *args, **options):
        # Check for migration changes
        self.stdout.write(self.style.SUCCESS('Checking for migration changes...'))
        logger.info('Checking for migration changes...')
        if self.check_pending_migrations():
            self.stdout.write(self.style.SUCCESS('Running pending migrations...'))
            logger.info('Running pending migrations...')
            call_command('migrate')

        # Collect static files
        self.stdout.write(self.style.SUCCESS('Collecting static files...'))
        logger.info('Collecting static files...')
        call_command('collectstatic', '--noinput')

        # Check and set up initial data if necessary
        self.stdout.write(self.style.SUCCESS('Checking for initial data setup...'))
        logger.info('Checking for initial data setup...')
        if self.check_for_initial_data():
            self.stdout.write(self.style.SUCCESS('Setting up initial data...'))
            logger.info('Setting up initial data...')
            self.setup_initial_data()
        else:
            self.stdout.write(self.style.SUCCESS('Initial data already exists.'))
            logger.info('Initial data already exists.')
