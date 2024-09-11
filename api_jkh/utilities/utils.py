from utilities.models import House, Payment


# Подсчет кварплаты за определенный месяц
def month_payment(data, pk):
    apartments = House.objects.get(pk=pk).apartment.all()
    for apartment in apartments:
        for wm in apartment.watermeter.all():
            month = wm.month.filter(month=data).first()
            if month:
                payment_for_water = month.quantity * apartment.apartment_rate.water_rate
                payment_for_maintenance = apartment.square * apartment.apartment_rate.maintenance
                payment = month.payment if hasattr(month, 'payment') else None
                if not payment:
                    payment = Payment(water_payment=payment_for_water, maintenance_payment=payment_for_maintenance,
                                      month_payment=month)
                payment.save()
    return {'OK': 200}
