from django.forms import ModelForm

from payment_credentials.models import WebPaymentLogModel


class WebPaymentLogForm(ModelForm):
    class Meta:
        model = WebPaymentLogModel
        fields = '__all__'
