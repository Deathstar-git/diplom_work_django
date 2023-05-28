from django.urls import path
from .views import *

urlpatterns = [
    path('', main, name='main'),
    path('multicookers', multicookers, name='multicookers'),
    path('mobile_phones', mobile_phones, name='mobile_phones'),
    path('fridge/<int:_id>/', fridge, name='fridge'),
    path('mobile_phone/<int:_id>/', mobile_phone, name='mobile_phone'),
    path('multicooker/<int:_id>/', multicooker, name='multicooker'),
    path('search/', search, name='search'),
    ]
