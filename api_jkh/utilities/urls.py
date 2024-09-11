from django.urls import path, include
from .views import *
app_name = 'utilities'

urlpatterns = [
    path('houses/', HouseApiView.as_view(), name='houses'),
    path('houses/<int:pk>/', HouseApiUpdateDeleteView.as_view(), name='update_house'),
    path('houses/<int:pk>/payment', payment_view, name='payment'),
    path('houses/payment', start_payment_task, name='all_payment'),
    path('apartments/', ApartmentApiView.as_view(), name='apartments'),
    path('apartments/<int:pk>/', HouseApiUpdateDeleteView.as_view(), name='update_apartment'),
    ]