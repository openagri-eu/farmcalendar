# Generated by Django 5.0.4 on 2024-11-30 13:44

import datetime
import django.core.validators
import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('farm_management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FarmCalendarActivity',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('start_datetime', models.DateTimeField(default=datetime.datetime.now)),
                ('end_datetime', models.DateTimeField(blank=True, null=True)),
                ('details', models.TextField(blank=True, null=True)),
                ('responsible_agent', models.CharField(blank=True, null=True)),
                ('agricultural_machinery', models.ManyToManyField(blank=True, related_name='used_in_operations', to='farm_management.agriculturalmachine')),
            ],
            options={
                'verbose_name': 'Farm Activity',
                'verbose_name_plural': 'Farm Activities',
            },
        ),
        migrations.CreateModel(
            name='FarmCalendarActivityType',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('background_color', models.CharField(default='#007bff', max_length=7, validators=[django.core.validators.RegexValidator(message='Enter a valid hex color code.', regex='^#[0-9A-Fa-f]{6}$')])),
                ('border_color', models.CharField(default='#007bff', max_length=7, validators=[django.core.validators.RegexValidator(message='Enter a valid hex color code.', regex='^#[0-9A-Fa-f]{6}$')])),
                ('text_color', models.CharField(default='#000000', max_length=7, validators=[django.core.validators.RegexValidator(message='Enter a valid hex color code.', regex='^#[0-9A-Fa-f]{6}$')])),
            ],
        ),
        migrations.CreateModel(
            name='Observation',
            fields=[
                ('farmcalendaractivity_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='farm_activities.farmcalendaractivity')),
                ('value', models.CharField(max_length=255)),
                ('value_unit', models.CharField(max_length=255)),
                ('observed_property', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Observation',
                'verbose_name_plural': 'Observations',
            },
            bases=('farm_activities.farmcalendaractivity',),
        ),
        migrations.AddField(
            model_name='farmcalendaractivity',
            name='activity_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farm_activities.farmcalendaractivitytype'),
        ),
        migrations.CreateModel(
            name='CropProtectionOperation',
            fields=[
                ('farmcalendaractivity_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='farm_activities.farmcalendaractivity')),
                ('applied_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('applied_amount_unit', models.CharField(max_length=255)),
                ('operated_on', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farm_management.farmparcel')),
                ('pesticide', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='farm_management.pesticide')),
            ],
            options={
                'verbose_name': 'Crop Protection Operation',
                'verbose_name_plural': 'Crop Protection Operations',
            },
            bases=('farm_activities.farmcalendaractivity',),
        ),
        migrations.CreateModel(
            name='FertilizationOperation',
            fields=[
                ('farmcalendaractivity_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='farm_activities.farmcalendaractivity')),
                ('applied_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('applied_amount_unit', models.CharField(max_length=255)),
                ('application_method', models.CharField(blank=True, max_length=255, null=True)),
                ('fertilizer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='farm_management.fertilizer')),
                ('operated_on', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farm_management.farmparcel')),
            ],
            options={
                'verbose_name': 'Fertilization Operation',
                'verbose_name_plural': 'Fertilization Operations',
            },
            bases=('farm_activities.farmcalendaractivity',),
        ),
        migrations.CreateModel(
            name='IrrigationOperation',
            fields=[
                ('farmcalendaractivity_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='farm_activities.farmcalendaractivity')),
                ('applied_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('applied_amount_unit', models.CharField(max_length=255)),
                ('irrigation_system', models.CharField(choices=[('sprinkler', 'Sprinkler'), ('drip', 'Drip'), ('centre_pivot', 'Centre Pivot'), ('furrow', 'Furrow'), ('terraced', 'Terraced')], default='sprinkler', max_length=50)),
                ('operated_on', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farm_management.farmparcel')),
            ],
            options={
                'verbose_name': 'Irrigation Operation',
                'verbose_name_plural': 'Irrigation Operations',
            },
            bases=('farm_activities.farmcalendaractivity',),
        ),
        migrations.CreateModel(
            name='CropGrowthStageObservation',
            fields=[
                ('observation_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='farm_activities.observation')),
                ('crop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farm_management.farmcrop')),
            ],
            options={
                'verbose_name': 'Crop Growth Stage Observation',
                'verbose_name_plural': 'Crop Growth Stage Observations',
            },
            bases=('farm_activities.observation',),
        ),
        migrations.CreateModel(
            name='CropStressIndicatorObservation',
            fields=[
                ('observation_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='farm_activities.observation')),
                ('crop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farm_management.farmcrop')),
            ],
            options={
                'verbose_name': 'Crop Stress Indicator Observation',
                'verbose_name_plural': 'Crop Stress Indicator Observations',
            },
            bases=('farm_activities.observation',),
        ),
    ]
