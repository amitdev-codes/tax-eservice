from django.urls import path
from ..views import property_views

urlpatterns = [
    path('land', property_views.land, name='land'),
    path('house', property_views.house_details, name='house_details'),
    path('house_floor', property_views.house_floor_details, name='house_floor_details'),
]
