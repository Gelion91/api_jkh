# Generated by Django 4.2 on 2024-09-11 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=100, verbose_name='Номер квартиры')),
                ('square', models.FloatField(verbose_name='Площадь квартиры')),
            ],
            options={
                'verbose_name': 'Квартира',
                'verbose_name_plural': 'Квартиры',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100, verbose_name='Адрес дома')),
                ('number', models.CharField(max_length=100, verbose_name='Номер дома')),
                ('date_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('date_update', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
            ],
            options={
                'verbose_name': 'Дом',
                'verbose_name_plural': 'Дома',
                'ordering': ['-date_create'],
            },
        ),
        migrations.CreateModel(
            name='Month',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(max_length=100, verbose_name='Месяц')),
                ('quantity', models.FloatField(default=0, verbose_name='Показания')),
            ],
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('water_rate', models.FloatField(verbose_name='Тариф за 1куб/м. воды')),
                ('maintenance', models.FloatField(verbose_name='Содержание общего имущества')),
                ('apartment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='apartment_rate', serialize=False, to='utilities.apartment')),
            ],
        ),
        migrations.CreateModel(
            name='WaterMeter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inventory_number', models.CharField(max_length=100, verbose_name='Инвентаризационный номер')),
                ('date_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('date_update', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('apartment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='watermeter', to='utilities.apartment', verbose_name='Квартира')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('water_payment', models.FloatField(verbose_name='Тариф за 1куб/м. воды')),
                ('maintenance_payment', models.FloatField(verbose_name='Содержание общего имущества')),
                ('month_payment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='payment', to='utilities.month')),
            ],
        ),
        migrations.AddField(
            model_name='month',
            name='water_meter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='month', to='utilities.watermeter', verbose_name='Счетчик'),
        ),
        migrations.AddField(
            model_name='apartment',
            name='house',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='apartment', to='utilities.house', verbose_name='Дом'),
        ),
    ]