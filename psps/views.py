from django.shortcuts import render
from django.urls import path, include

# Create your views here.
path('esewa/', include('psps.views.esewa_views')),
path('khalti/', include('psps.views.khalti_views')),
path('ips/', include('psps.views.ips_views')),
path('fonepay/', include('psps.views.fonepay_views')),
