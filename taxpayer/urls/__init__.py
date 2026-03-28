from django.urls import path, include

urlpatterns = [
    path('app/', include('taxpayer.urls.information_urls')),
    path('property/', include('taxpayer.urls.property_urls')),
]
