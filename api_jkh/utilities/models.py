from django.db import models


class House(models.Model):
    address = models.CharField(max_length=100, verbose_name='Адрес дома', null=False)
    number = models.CharField(max_length=100, verbose_name='Номер дома')
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    date_update = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    class Meta:
        verbose_name = 'Дом'
        verbose_name_plural = 'Дома'
        ordering = ['-date_create']

    def __str__(self):
        if self.address and self.number:
            return f'{self.address} {self.number}'
        return self.address


class Apartment(models.Model):
    number = models.CharField(max_length=100, verbose_name='Номер квартиры', null=False)
    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name='apartment', verbose_name='Дом')
    square = models.FloatField(verbose_name='Площадь квартиры', null=False)

    class Meta:
        verbose_name = 'Квартира'
        verbose_name_plural = 'Квартиры'
        ordering = ['-id']

    def __str__(self):
        if self.number:
            return f'{self.house}, квартира:{self.number}'


class WaterMeter(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, related_name='watermeter',
                                  verbose_name='Квартира')
    inventory_number = models.CharField(max_length=100, verbose_name='Инвентаризационный номер')
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    date_update = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    class Meta:
        verbose_name = 'Счетчик'
        verbose_name_plural = 'счетчики'
        ordering = ['-date_create']

    def __str__(self):
        if self.inventory_number:
            return self.inventory_number
        return self.pk


class Month(models.Model):
    month = models.CharField(max_length=100, verbose_name='Месяц', null=False)
    water_meter = models.ForeignKey(WaterMeter, on_delete=models.CASCADE, related_name='month',
                                         verbose_name='Счетчик')
    quantity = models.FloatField(verbose_name='Показания', default=0)

    class Meta:
        verbose_name = 'Месяц'
        verbose_name_plural = 'Месяцы'
        ordering = ['-id']

    def __str__(self):
        if self.month:
            return self.month
        return self.pk


class Rate(models.Model):
    water_rate = models.FloatField(verbose_name='Тариф за 1куб/м. воды')
    maintenance = models.FloatField(verbose_name='Содержание общего имущества')
    apartment = models.OneToOneField(Apartment, on_delete=models.CASCADE, related_name="apartment_rate",
                                     primary_key=True)

    class Meta:
        verbose_name = 'Тариф'
        verbose_name_plural = 'Тарифы'
        ordering = ['-id']


class Payment(models.Model):
    water_payment = models.FloatField(verbose_name='Тариф за 1куб/м. воды')
    maintenance_payment = models.FloatField(verbose_name='Содержание общего имущества')
    month_payment = models.OneToOneField(Month, on_delete=models.CASCADE, related_name="payment")

    class Meta:
        verbose_name = 'Оплата'
        verbose_name_plural = 'Оплаты'
        ordering = ['-id']