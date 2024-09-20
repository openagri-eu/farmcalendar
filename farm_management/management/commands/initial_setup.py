from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.db import connections
from django.db.migrations.executor import MigrationExecutor
from django.db.migrations.recorder import MigrationRecorder

from django.conf import settings

from farm_operations.models import FarmOperationType



class Command(BaseCommand):
    help = "Initial setup command, based on the same one in gatekeeper's command"


    def check_for_initial_data(self):
        return len(FarmOperationType.objects.all()) == 0

    def setup_initial_data(self):
        for def_operation_type in settings.DEFAULT_OPERATION_TYPES.values():
            operation = FarmOperationType(
                **def_operation_type,
            ).save()

    def check_pending_migrations(self):
        for connection in connections.all():
            executor = MigrationExecutor(connection)
            targets = executor.loader.graph.leaf_nodes()
            recorder = MigrationRecorder(connection)
            applied = recorder.applied_migrations()

            unapplied = [migration for migration in targets if migration not in applied]

            return len(unapplied) > 0


    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Checking for migration changes...'))

        if self.check_pending_migrations():
            self.stdout.write(self.style.SUCCESS('Pending migrations detected, running migrations...'))
            call_command('migrate')

        self.stdout.write(self.style.SUCCESS('Collecting static files...'))
        call_command('collectstatic', '--noinput')

        #  maybe this should be a data migration in the end, but during this
        #  early dev processs its best to leave it independent of migrations
        self.stdout.write(self.style.SUCCESS('checking for initial data setup'))
        if self.check_for_initial_data():
            self.stdout.write(self.style.SUCCESS('Pending initial data setup, will setup initial data now.'))
            self.setup_initial_data()


