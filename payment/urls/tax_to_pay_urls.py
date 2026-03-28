from django.urls import path

from ..views import tax_to_pay_views
from ..views import tax_paid_views

urlpatterns = [
    path('tax_to_pay', tax_to_pay_views.tax_to_pay, name='tax_to_pay'),
    path('initiate_payment', tax_to_pay_views.initiate_payment, name='initiate_payment'),
    path('tax_paid', tax_paid_views.tax_paid, name='tax_paid'),
]
