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

# Set up logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class Command(BaseCommand):
    help = "Initial setup command, based on the same one in gatekeeper's command"

    # Check if there is any existing data for AdminMenuMaster or FarmCalendarActivityType
    def check_for_initial_data(self):
        return not FarmCalendarActivityType.objects.exists()

    def setup_initial_data(self):
        # Populate FarmCalendarActivityType
        self.stdout.write(self.style.SUCCESS('Setting up FarmCalendarActivityType data...'))
        for def_operation_type in settings.DEFAULT_CALENDAR_ACTIVITY_TYPES.values():
            operation = FarmCalendarActivityType(**def_operation_type)
            operation.save()

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
