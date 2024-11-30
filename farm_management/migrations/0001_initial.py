# Generated by Django 5.0.4 on 2024-11-30 13:44

import django.db.models.deletion
import simple_history.models
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Farm',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(0, 'Inactive'), (1, 'Active'), (2, 'Deleted')], default=1, verbose_name='Status')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Deleted At')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('name', models.CharField(default='Unnamed Farm', max_length=255, verbose_name='Farm Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Farm Description')),
                ('administrator', models.CharField(blank=True, max_length=255, null=True, verbose_name='Farm Administrator')),
                ('contact_person_firstname', models.CharField(blank=True, max_length=255, null=True, verbose_name='Contact Person First Name')),
                ('contact_person_lastname', models.CharField(blank=True, max_length=255, null=True, verbose_name='Contact Person Last Name')),
                ('telephone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Contact Telephone')),
                ('vat_id', models.CharField(blank=True, max_length=50, null=True, verbose_name='VAT ID')),
                ('admin_unit_l1', models.CharField(blank=True, max_length=255, null=True, verbose_name='Admin Unit Line 1')),
                ('admin_unit_l2', models.CharField(blank=True, max_length=255, null=True, verbose_name='Admin Unit Line 2')),
                ('address_area', models.CharField(blank=True, max_length=255, null=True, verbose_name='Address Area')),
                ('municipality', models.CharField(blank=True, max_length=255, null=True, verbose_name='Municipality')),
                ('community', models.CharField(blank=True, max_length=255, null=True, verbose_name='Community')),
                ('locator_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Locator Name')),
            ],
            options={
                'verbose_name': 'Farm',
                'verbose_name_plural': 'Farms',
            },
        ),
        migrations.CreateModel(
            name='Fertilizer',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(0, 'Inactive'), (1, 'Active'), (2, 'Deleted')], default=1, verbose_name='Status')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Deleted At')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('price_unit', models.CharField(max_length=255)),
                ('active_substance', models.CharField(max_length=255)),
                ('targeted_towards', models.CharField(max_length=255)),
                ('nutrient_concentration', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
            options={
                'verbose_name': 'Fertilizer',
                'verbose_name_plural': 'Fertilizers',
            },
        ),
        migrations.CreateModel(
            name='Pesticide',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(0, 'Inactive'), (1, 'Active'), (2, 'Deleted')], default=1, verbose_name='Status')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Deleted At')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('price_unit', models.CharField(max_length=255)),
                ('active_substance', models.CharField(max_length=255)),
                ('targeted_towards', models.CharField(max_length=255)),
                ('preharvest_interval', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Pesticide',
                'verbose_name_plural': 'Pesticides',
            },
        ),
        migrations.CreateModel(
            name='FarmParcel',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(0, 'Inactive'), (1, 'Active'), (2, 'Deleted')], default=1, verbose_name='Status')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Deleted At')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('latitude', models.DecimalField(blank=True, decimal_places=14, max_digits=17, null=True, verbose_name='Latitude')),
                ('longitude', models.DecimalField(blank=True, decimal_places=14, max_digits=17, null=True, verbose_name='Longitude')),
                ('geometry', models.TextField(blank=True, null=True, verbose_name='Geometry (WKT EPSG:4326)')),
                ('geo_id', models.UUIDField(blank=True, null=True, unique=True, verbose_name='Geographic Data ID')),
                ('identifier', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('parcel_type', models.CharField(max_length=50, verbose_name='Type of Parcel')),
                ('valid_from', models.DateTimeField(blank=True, null=True)),
                ('valid_to', models.DateTimeField(blank=True, null=True)),
                ('in_region', models.CharField(blank=True, max_length=255, null=True)),
                ('has_toponym', models.CharField(blank=True, max_length=255, null=True)),
                ('area', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
                ('is_nitro_area', models.BooleanField(default=False)),
                ('is_natura2000_area', models.BooleanField(default=False)),
                ('is_pdopg_area', models.BooleanField(default=False)),
                ('is_irrigated', models.BooleanField(default=False)),
                ('is_cultivated_in_levels', models.BooleanField(default=False)),
                ('is_ground_slope', models.BooleanField(default=False)),
                ('depiction', models.URLField(blank=True, max_length=500, null=True)),
                ('irrigation_flow', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('farm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='farm_parcels', to='farm_management.farm')),
            ],
            options={
                'verbose_name': 'Farm Parcel',
                'verbose_name_plural': 'Farm Parcels',
            },
        ),
        migrations.CreateModel(
            name='FarmCrop',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(0, 'Inactive'), (1, 'Active'), (2, 'Deleted')], default=1, verbose_name='Status')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Deleted At')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('species', models.CharField(max_length=255)),
                ('variety', models.CharField(blank=True, max_length=255, null=True)),
                ('growth_stage', models.CharField(blank=True, max_length=255, null=True)),
                ('parcel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)ss', to='farm_management.farmparcel')),
            ],
            options={
                'verbose_name': 'Farm Plant',
                'verbose_name_plural': 'Farm Plants',
            },
        ),
        migrations.CreateModel(
            name='FarmAnimal',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(0, 'Inactive'), (1, 'Active'), (2, 'Deleted')], default=1, verbose_name='Status')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Deleted At')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('species', models.CharField(max_length=255)),
                ('breed', models.CharField(blank=True, max_length=255, null=True)),
                ('birth_date', models.DateTimeField()),
                ('sex', models.IntegerField(choices=[(0, 'N/A'), (1, 'Female'), (2, 'Male')], default=0)),
                ('age', models.IntegerField(default=0)),
                ('number_of_animals', models.IntegerField(default=1)),
                ('castrated', models.BooleanField(default=False)),
                ('parcel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)ss', to='farm_management.farmparcel')),
            ],
            options={
                'verbose_name': 'Farm Animal',
                'verbose_name_plural': 'Farm Animals',
            },
        ),
        migrations.CreateModel(
            name='AgriculturalMachine',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(0, 'Inactive'), (1, 'Active'), (2, 'Deleted')], default=1, verbose_name='Status')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Deleted At')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('purchase_date', models.DateField()),
                ('manufacturer', models.CharField(max_length=255)),
                ('model', models.CharField(max_length=255)),
                ('seria_number', models.CharField(max_length=255)),
                ('parcel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)ss', to='farm_management.farmparcel')),
            ],
            options={
                'verbose_name': 'Farm Equipment',
                'verbose_name_plural': 'Farm Equipments',
            },
        ),
        migrations.CreateModel(
            name='FarmSensor',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(0, 'Inactive'), (1, 'Active'), (2, 'Deleted')], default=1, verbose_name='Status')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Deleted At')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('sensor_type', models.CharField()),
                ('public', models.BooleanField(default=False)),
                ('parcel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)ss', to='farm_management.farmparcel')),
            ],
            options={
                'verbose_name': 'Farm Sensor',
                'verbose_name_plural': 'Farm Sensors',
            },
        ),
        migrations.CreateModel(
            name='HistoricalAgriculturalMachine',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(0, 'Inactive'), (1, 'Active'), (2, 'Deleted')], default=1, verbose_name='Status')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Deleted At')),
                ('created_at', models.DateTimeField(blank=True, editable=False, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(blank=True, editable=False, verbose_name='Updated At')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('purchase_date', models.DateField()),
                ('manufacturer', models.CharField(max_length=255)),
                ('model', models.CharField(max_length=255)),
                ('seria_number', models.CharField(max_length=255)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('parcel', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='farm_management.farmparcel')),
            ],
            options={
                'verbose_name': 'historical Farm Equipment',
                'verbose_name_plural': 'historical Farm Equipments',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalFarm',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(0, 'Inactive'), (1, 'Active'), (2, 'Deleted')], default=1, verbose_name='Status')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Deleted At')),
                ('created_at', models.DateTimeField(blank=True, editable=False, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(blank=True, editable=False, verbose_name='Updated At')),
                ('name', models.CharField(default='Unnamed Farm', max_length=255, verbose_name='Farm Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Farm Description')),
                ('administrator', models.CharField(blank=True, max_length=255, null=True, verbose_name='Farm Administrator')),
                ('contact_person_firstname', models.CharField(blank=True, max_length=255, null=True, verbose_name='Contact Person First Name')),
                ('contact_person_lastname', models.CharField(blank=True, max_length=255, null=True, verbose_name='Contact Person Last Name')),
                ('telephone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Contact Telephone')),
                ('vat_id', models.CharField(blank=True, max_length=50, null=True, verbose_name='VAT ID')),
                ('admin_unit_l1', models.CharField(blank=True, max_length=255, null=True, verbose_name='Admin Unit Line 1')),
                ('admin_unit_l2', models.CharField(blank=True, max_length=255, null=True, verbose_name='Admin Unit Line 2')),
                ('address_area', models.CharField(blank=True, max_length=255, null=True, verbose_name='Address Area')),
                ('municipality', models.CharField(blank=True, max_length=255, null=True, verbose_name='Municipality')),
                ('community', models.CharField(blank=True, max_length=255, null=True, verbose_name='Community')),
                ('locator_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Locator Name')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Farm',
                'verbose_name_plural': 'historical Farms',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalFarmAnimal',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(0, 'Inactive'), (1, 'Active'), (2, 'Deleted')], default=1, verbose_name='Status')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Deleted At')),
                ('created_at', models.DateTimeField(blank=True, editable=False, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(blank=True, editable=False, verbose_name='Updated At')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('species', models.CharField(max_length=255)),
                ('breed', models.CharField(blank=True, max_length=255, null=True)),
                ('birth_date', models.DateTimeField()),
                ('sex', models.IntegerField(choices=[(0, 'N/A'), (1, 'Female'), (2, 'Male')], default=0)),
                ('age', models.IntegerField(default=0)),
                ('number_of_animals', models.IntegerField(default=1)),
                ('castrated', models.BooleanField(default=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('parcel', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='farm_management.farmparcel')),
            ],
            options={
                'verbose_name': 'historical Farm Animal',
                'verbose_name_plural': 'historical Farm Animals',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalFarmCrop',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(0, 'Inactive'), (1, 'Active'), (2, 'Deleted')], default=1, verbose_name='Status')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Deleted At')),
                ('created_at', models.DateTimeField(blank=True, editable=False, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(blank=True, editable=False, verbose_name='Updated At')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('species', models.CharField(max_length=255)),
                ('variety', models.CharField(blank=True, max_length=255, null=True)),
                ('growth_stage', models.CharField(blank=True, max_length=255, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('parcel', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='farm_management.farmparcel')),
            ],
            options={
                'verbose_name': 'historical Farm Plant',
                'verbose_name_plural': 'historical Farm Plants',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalFarmParcel',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(0, 'Inactive'), (1, 'Active'), (2, 'Deleted')], default=1, verbose_name='Status')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Deleted At')),
                ('created_at', models.DateTimeField(blank=True, editable=False, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(blank=True, editable=False, verbose_name='Updated At')),
                ('latitude', models.DecimalField(blank=True, decimal_places=14, max_digits=17, null=True, verbose_name='Latitude')),
                ('longitude', models.DecimalField(blank=True, decimal_places=14, max_digits=17, null=True, verbose_name='Longitude')),
                ('geometry', models.TextField(blank=True, null=True, verbose_name='Geometry (WKT EPSG:4326)')),
                ('geo_id', models.UUIDField(blank=True, db_index=True, null=True, verbose_name='Geographic Data ID')),
                ('identifier', models.CharField(db_index=True, max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('parcel_type', models.CharField(max_length=50, verbose_name='Type of Parcel')),
                ('valid_from', models.DateTimeField(blank=True, null=True)),
                ('valid_to', models.DateTimeField(blank=True, null=True)),
                ('in_region', models.CharField(blank=True, max_length=255, null=True)),
                ('has_toponym', models.CharField(blank=True, max_length=255, null=True)),
                ('area', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
                ('is_nitro_area', models.BooleanField(default=False)),
                ('is_natura2000_area', models.BooleanField(default=False)),
                ('is_pdopg_area', models.BooleanField(default=False)),
                ('is_irrigated', models.BooleanField(default=False)),
                ('is_cultivated_in_levels', models.BooleanField(default=False)),
                ('is_ground_slope', models.BooleanField(default=False)),
                ('depiction', models.URLField(blank=True, max_length=500, null=True)),
                ('irrigation_flow', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('farm', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='farm_management.farm')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Farm Parcel',
                'verbose_name_plural': 'historical Farm Parcels',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalFarmSensor',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(0, 'Inactive'), (1, 'Active'), (2, 'Deleted')], default=1, verbose_name='Status')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Deleted At')),
                ('created_at', models.DateTimeField(blank=True, editable=False, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(blank=True, editable=False, verbose_name='Updated At')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('sensor_type', models.CharField()),
                ('public', models.BooleanField(default=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('parcel', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='farm_management.farmparcel')),
            ],
            options={
                'verbose_name': 'historical Farm Sensor',
                'verbose_name_plural': 'historical Farm Sensors',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalFertilizer',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(0, 'Inactive'), (1, 'Active'), (2, 'Deleted')], default=1, verbose_name='Status')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Deleted At')),
                ('created_at', models.DateTimeField(blank=True, editable=False, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(blank=True, editable=False, verbose_name='Updated At')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('price_unit', models.CharField(max_length=255)),
                ('active_substance', models.CharField(max_length=255)),
                ('targeted_towards', models.CharField(max_length=255)),
                ('nutrient_concentration', models.DecimalField(decimal_places=2, max_digits=5)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Fertilizer',
                'verbose_name_plural': 'historical Fertilizers',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalPesticide',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(0, 'Inactive'), (1, 'Active'), (2, 'Deleted')], default=1, verbose_name='Status')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Deleted At')),
                ('created_at', models.DateTimeField(blank=True, editable=False, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(blank=True, editable=False, verbose_name='Updated At')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('price_unit', models.CharField(max_length=255)),
                ('active_substance', models.CharField(max_length=255)),
                ('targeted_towards', models.CharField(max_length=255)),
                ('preharvest_interval', models.IntegerField(default=0)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Pesticide',
                'verbose_name_plural': 'historical Pesticides',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
