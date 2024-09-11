from rest_framework import serializers
from .models import House, Apartment, WaterMeter, Month, Rate, Payment
from drf_writable_nested import WritableNestedModelSerializer


class RateSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = ['water_rate', 'maintenance']


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['water_payment', 'maintenance_payment']


class MonthSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    payment = PaymentSerializer()

    class Meta:
        model = Month
        fields = ['month', 'quantity', 'payment']


class WaterMeterSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    month = MonthSerializer(many=True)

    class Meta:
        model = WaterMeter
        fields = ['id', 'inventory_number', 'month']


class ApartmentSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    watermeter = WaterMeterSerializer(many=True)
    apartment_rate = RateSerializer()

    class Meta:
        model = Apartment
        fields = "__all__"


class HouseSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    apartment = ApartmentSerializer(many=True)

    class Meta:
        model = House
        fields = '__all__'

