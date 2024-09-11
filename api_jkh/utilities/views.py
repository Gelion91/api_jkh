from asgiref.sync import sync_to_async
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from utilities.models import House, Apartment, Payment
from utilities.serializers import HouseSerializer, ApartmentSerializer
from .tasks import get_all_payment
from .utils import month_payment


# Апи вывода домов со всеми отношениями
class HouseApiView(generics.ListCreateAPIView):
    queryset = House.objects.all()
    serializer_class = HouseSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


# Апи вывода дома по id со всеми отношениями
class HouseApiUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = House.objects.all()
    serializer_class = HouseSerializer


# Апи вывода квартир со всеми отношениями
class ApartmentApiView(generics.ListCreateAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer


# Апи вывода квартиры по id со всеми отношениями
class ApartmentApiUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer


# Функция просчета кварплаты по месяцам
@sync_to_async
@api_view(["GET"])
def payment_view(request, pk):
    data = request.GET.get('date', None)
    if data:
        result = month_payment(data, pk)
        return Response(result)
    return Response({'ERROR': 'Необходимо передать QueryParam в виде ?date=month'})

# Запуск таски на просчет кварплаты
@sync_to_async
@api_view(["GET"])
def start_payment_task(request):
    result = get_all_payment.delay()
    return Response(result)

