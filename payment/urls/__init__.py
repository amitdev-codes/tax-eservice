from django.urls import path, include

urlpatterns = [
    path('payment/', include('payment.urls.tax_to_pay_urls')),
    path('psps/', include('payment.urls.psp_urls')),
]
