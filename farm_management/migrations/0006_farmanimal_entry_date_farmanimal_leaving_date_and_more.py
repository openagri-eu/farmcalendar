# Generated by Django 5.0.4 on 2025-04-24 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farm_management', '0005_genericfarmasset_historicalgenericfarmasset'),
    ]

    operations = [
        migrations.AddField(
            model_name='farmanimal',
            name='entry_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='farmanimal',
            name='leaving_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='farmanimal',
            name='previous_owner',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='historicalfarmanimal',
            name='entry_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='historicalfarmanimal',
            name='leaving_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='historicalfarmanimal',
            name='previous_owner',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
