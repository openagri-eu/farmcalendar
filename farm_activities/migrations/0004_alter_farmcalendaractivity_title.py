# Generated by Django 5.0.4 on 2025-02-27 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farm_activities', '0003_compostoperation_compostturningoperation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmcalendaractivity',
            name='title',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
