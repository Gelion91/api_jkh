from celery import shared_task

from utilities.models import House, Payment


@shared_task
def get_all_payment():
    houses = House.objects.all()
    for house in houses:
        apartments = house.apartment.all()
        for apartment in apartments:
            for wm in apartment.watermeter.all():
                months = wm.month.all()
                for month in months:
                    if month:
                        payment_for_water = month.quantity * apartment.apartment_rate.water_rate
                        payment_for_maintenance = apartment.square * apartment.apartment_rate.maintenance
                        payment = month.payment if hasattr(month, 'payment') else None
                        if not payment:
                            payment = Payment(water_payment=payment_for_water,
                                              maintenance_payment=payment_for_maintenance,
                                              month_payment=month
                                              )
                        payment.save()
    return {'OK': 200}
