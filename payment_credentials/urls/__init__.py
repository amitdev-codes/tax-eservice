from django.urls import path, include

urlpatterns = [
    path('payments/', include('payment_credentials.urls.payment_urls')),
]
