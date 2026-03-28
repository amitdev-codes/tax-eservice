from django.urls import path, include

urlpatterns = [
    path('esewa/', include('psps.urls.esewa_urls')),
    path('ips/', include('psps.urls.ips_urls')),
    path('khalti/', include('psps.urls.khalti_urls')),
    path('fonepay/', include('psps.urls.fonepay_urls')),
]
