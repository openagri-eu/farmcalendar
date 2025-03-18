# Generated by Django 5.0.4 on 2025-03-18 09:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farm_activities', '0005_observation_sensor_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='NPKObservationCollection',
            fields=[
                ('observation_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='farm_activities.observation')),
                ('value2', models.CharField(max_length=255)),
                ('value_unit2', models.CharField(blank=True, max_length=255, null=True)),
                ('observed_property2', models.CharField(max_length=255)),
                ('value3', models.CharField(max_length=255)),
                ('value_unit3', models.CharField(blank=True, max_length=255, null=True)),
                ('observed_property3', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'NPK Observation Collection',
                'verbose_name_plural': 'NPK Observation Collections',
            },
            bases=('farm_activities.observation',),
        ),
    ]
