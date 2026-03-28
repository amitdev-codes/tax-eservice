from django.forms import ModelForm

from master_menu.models import AppClientSettingModel,  MstUserType, MstTaxTypeOnlinePayment, \
    MstThirdParty, MstPaymentWallet, AccReceiptFlagModel


class AppClientSettingForm(ModelForm):
    class Meta:
        model = AppClientSettingModel
        fields = '__all__'


class AccReceiptFlagForm(ModelForm):
    class Meta:
        model = AccReceiptFlagModel
        fields = '__all__'


class MstUserTypeForm(ModelForm):
    class Meta:
        model = MstUserType
        fields = '__all__'


class MstTaxTypeOnlinePaymentForm(ModelForm):
    class Meta:
        model = MstTaxTypeOnlinePayment
        fields = '__all__'


class MstThirdPartyForm(ModelForm):
    class Meta:
        model = MstThirdParty
        fields = '__all__'


class MstPaymentWalletForm(ModelForm):
    class Meta:
        model = MstPaymentWallet
        fields = '__all__'
