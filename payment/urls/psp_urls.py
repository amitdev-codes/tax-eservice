from django.urls import path

from ..views import tax_to_pay_views
from ..views import tax_paid_views

urlpatterns = [
    path('psp_payment', tax_to_pay_views.redirect_psp, name='psp_payment'),
]
