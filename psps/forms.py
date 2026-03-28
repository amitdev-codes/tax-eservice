from django.forms import ModelForm
from .models import EsewaWebCredential, KhaltiWebCredential, IpsWebCredential, VwAppClientModel, FonepayWebCredential


class EsewaForm(ModelForm):
    class Meta:
        model = EsewaWebCredential
        fields = '__all__'


class IpsForm(ModelForm):
    class Meta:
        model = IpsWebCredential
        fields = '__all__'


class KhaltiForm(ModelForm):
    class Meta:
        model = KhaltiWebCredential
        fields = '__all__'


class FonepayForm(ModelForm):
    class Meta:
        model = FonepayWebCredential
        fields = '__all__'
