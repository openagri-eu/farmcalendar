# Generated by Django 5.0.4 on 2024-09-19 16:21

import django.db.models.deletion
import simple_history.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FarmParcel',
            fields=[
                ('id', models.AutoField(db_index=True, editable=False, primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('status', models.IntegerField(choices=[(0, 'Active'), (1, 'Deleted')], default=0)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('geo_id', models.UUIDField(blank=True, null=True, verbose_name='Georaphic Data ID')),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Farm Parcel',
                'verbose_name_plural': 'Farm Parcels',
            },
        ),
        migrations.CreateModel(
            name='FarmEquipment',
            fields=[
                ('id', models.AutoField(db_index=True, editable=False, primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('status', models.IntegerField(choices=[(0, 'Active'), (1, 'Deleted')], default=0)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('geo_id', models.UUIDField(blank=True, null=True, verbose_name='Geographic Data ID')),
                ('purchase_date', models.DateField()),
                ('manufacturer', models.CharField(max_length=255)),
                ('model', models.CharField(max_length=255)),
                ('seria_number', models.CharField(max_length=255)),
                ('area', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)ss', to='farm_management.farmparcel')),
            ],
            options={
                'verbose_name': 'Farm Equipment',
                'verbose_name_plural': 'Farm Equipments',
            },
        ),
        migrations.CreateModel(
            name='FarmAnimal',
            fields=[
                ('id', models.AutoField(db_index=True, editable=False, primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('status', models.IntegerField(choices=[(0, 'Active'), (1, 'Deleted')], default=0)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('geo_id', models.UUIDField(blank=True, null=True, verbose_name='Geographic Data ID')),
                ('sex', models.IntegerField(choices=[(0, 'N/A'), (1, 'Female'), (2, 'Male')], default=0)),
                ('castrated', models.BooleanField(default=False)),
                ('species', models.CharField(max_length=255)),
                ('breed', models.CharField(blank=True, max_length=255, null=True)),
                ('birth_date', models.DateTimeField()),
                ('area', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)ss', to='farm_management.farmparcel')),
            ],
            options={
                'verbose_name': 'Farm Animal',
                'verbose_name_plural': 'Farm Animals',
            },
        ),
        migrations.CreateModel(
            name='FarmPlant',
            fields=[
                ('id', models.AutoField(db_index=True, editable=False, primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('status', models.IntegerField(choices=[(0, 'Active'), (1, 'Deleted')], default=0)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('geo_id', models.UUIDField(blank=True, null=True, verbose_name='Geographic Data ID')),
                ('species', models.CharField(max_length=255)),
                ('variety', models.CharField(blank=True, max_length=255, null=True)),
                ('area', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)ss', to='farm_management.farmparcel')),
            ],
            options={
                'verbose_name': 'Farm Plant',
                'verbose_name_plural': 'Farm Plants',
            },
        ),
        migrations.CreateModel(
            name='FarmSensor',
            fields=[
                ('id', models.AutoField(db_index=True, editable=False, primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('status', models.IntegerField(choices=[(0, 'Active'), (1, 'Deleted')], default=0)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('geo_id', models.UUIDField(blank=True, null=True, verbose_name='Geographic Data ID')),
                ('sensor_type', models.CharField()),
                ('public', models.BooleanField(default=False)),
                ('area', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)ss', to='farm_management.farmparcel')),
            ],
            options={
                'verbose_name': 'Farm Sensor',
                'verbose_name_plural': 'Farm Sensors',
            },
        ),
        migrations.CreateModel(
            name='HistoricalFarmAnimal',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True, editable=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('status', models.IntegerField(choices=[(0, 'Active'), (1, 'Deleted')], default=0)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(blank=True, editable=False)),
                ('updated_at', models.DateTimeField(blank=True, editable=False)),
                ('description', models.TextField(blank=True, null=True)),
                ('geo_id', models.UUIDField(blank=True, null=True, verbose_name='Geographic Data ID')),
                ('sex', models.IntegerField(choices=[(0, 'N/A'), (1, 'Female'), (2, 'Male')], default=0)),
                ('castrated', models.BooleanField(default=False)),
                ('species', models.CharField(max_length=255)),
                ('breed', models.CharField(blank=True, max_length=255, null=True)),
                ('birth_date', models.DateTimeField()),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('area', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='farm_management.farmparcel')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
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
            name='HistoricalFarmEquipment',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True, editable=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('status', models.IntegerField(choices=[(0, 'Active'), (1, 'Deleted')], default=0)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(blank=True, editable=False)),
                ('updated_at', models.DateTimeField(blank=True, editable=False)),
                ('description', models.TextField(blank=True, null=True)),
                ('geo_id', models.UUIDField(blank=True, null=True, verbose_name='Geographic Data ID')),
                ('purchase_date', models.DateField()),
                ('manufacturer', models.CharField(max_length=255)),
                ('model', models.CharField(max_length=255)),
                ('seria_number', models.CharField(max_length=255)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('area', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='farm_management.farmparcel')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
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
            name='HistoricalFarmParcel',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True, editable=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('status', models.IntegerField(choices=[(0, 'Active'), (1, 'Deleted')], default=0)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(blank=True, editable=False)),
                ('updated_at', models.DateTimeField(blank=True, editable=False)),
                ('geo_id', models.UUIDField(blank=True, null=True, verbose_name='Georaphic Data ID')),
                ('description', models.TextField(blank=True, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
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
            name='HistoricalFarmPlant',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True, editable=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('status', models.IntegerField(choices=[(0, 'Active'), (1, 'Deleted')], default=0)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(blank=True, editable=False)),
                ('updated_at', models.DateTimeField(blank=True, editable=False)),
                ('description', models.TextField(blank=True, null=True)),
                ('geo_id', models.UUIDField(blank=True, null=True, verbose_name='Geographic Data ID')),
                ('species', models.CharField(max_length=255)),
                ('variety', models.CharField(blank=True, max_length=255, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('area', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='farm_management.farmparcel')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
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
            name='HistoricalFarmSensor',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True, editable=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('status', models.IntegerField(choices=[(0, 'Active'), (1, 'Deleted')], default=0)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(blank=True, editable=False)),
                ('updated_at', models.DateTimeField(blank=True, editable=False)),
                ('description', models.TextField(blank=True, null=True)),
                ('geo_id', models.UUIDField(blank=True, null=True, verbose_name='Geographic Data ID')),
                ('sensor_type', models.CharField()),
                ('public', models.BooleanField(default=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('area', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='farm_management.farmparcel')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Farm Sensor',
                'verbose_name_plural': 'historical Farm Sensors',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
