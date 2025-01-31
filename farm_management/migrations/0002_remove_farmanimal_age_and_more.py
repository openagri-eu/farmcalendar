# Generated by Django 5.0.4 on 2025-01-31 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farm_management', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='farmanimal',
            name='age',
        ),
        migrations.RemoveField(
            model_name='farmanimal',
            name='number_of_animals',
        ),
        migrations.RemoveField(
            model_name='historicalfarmanimal',
            name='age',
        ),
        migrations.RemoveField(
            model_name='historicalfarmanimal',
            name='number_of_animals',
        ),
        migrations.AddField(
            model_name='farmanimal',
            name='animal_group',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='farmanimal',
            name='national_id',
            field=models.CharField(blank=True, null=True, verbose_name='National ID'),
        ),
        migrations.AddField(
            model_name='historicalfarmanimal',
            name='animal_group',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='historicalfarmanimal',
            name='national_id',
            field=models.CharField(blank=True, null=True, verbose_name='National ID'),
        ),
        migrations.AlterField(
            model_name='farmanimal',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='historicalfarmanimal',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Name'),
        ),
    ]
