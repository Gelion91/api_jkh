# Generated by Django 4.2 on 2024-09-11 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('utilities', '0002_remove_month_water_meter_month_water_meter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='month',
            name='water_meter',
        ),
        migrations.AddField(
            model_name='month',
            name='water_meter',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='month', to='utilities.watermeter', verbose_name='Счетчик'),
            preserve_default=False,
        ),
    ]
