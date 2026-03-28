from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from master_menu.models import MstPaymentWallet, AppSettingMaster, VwAppClientwiseSetting, VwMstCountry, \
    VwAppClient, TaxTypes, MstTaxTypeOnlinePayment
from master_menu.forms import MstPaymentWalletForm
from psps.models import VwAppClientModel


class PaymentWalletListView(ListView):
    model = MstPaymentWallet
    template_name = 'master_menu/templates/mst_payment_wallets/index.html'
    context_object_name = 'credentials'


class PaymentWalletDetailView(DetailView):
    model = MstPaymentWallet
    template_name = 'master_menu/templates/mst_payment_wallets/detail.html'
    context_object_name = 'credential'


class PaymentWalletCreateView(CreateView):
    model = MstPaymentWallet
    form_class = MstPaymentWalletForm
    template_name = 'master_menu/templates/mst_payment_wallets/create.html'
    success_url = '/client_settings/mst_payment_wallets'  # Redirects to the list view after successful creation

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        clients = VwAppClientModel.objects.values_list('id', 'name_en', 'name_np').order_by('name_en')
        context['clients'] = list(clients)

        online_payable_taxes = MstTaxTypeOnlinePayment.objects.filter(is_active=True).values_list('tax_type_id',
                                                                                                  flat=True)
        online_payable_taxes = list(online_payable_taxes)
        tax_types = TaxTypes.objects.filter(id__in=online_payable_taxes, is_deleted=False).values_list('id', 'name_en',
                                                                                                       'name_np').order_by(
            'name_en')
        context['tax_types'] = list(tax_types)
        return context


class PaymentWalletUpdateView(UpdateView):
    model = MstPaymentWallet
    form_class = MstPaymentWalletForm
    template_name = 'master_menu/templates/mst_payment_wallets/update.html'
    success_url = '/client_settings/mst_payment_wallets'  # Redirects to the list view after successful update

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        clients = VwAppClientModel.objects.values_list('id', 'name_en', 'name_np').order_by('name_en')
        context['clients'] = list(clients)

        tax_types = TaxTypes.objects.filter(is_deleted=False).values_list('id', 'name_en', 'name_np').order_by(
            'name_en')
        context['tax_types'] = list(tax_types)
        return context


class PaymentWalletDeleteView(DeleteView):
    model = MstPaymentWallet
    success_url = '/client_settings/mst_payment_wallets'


class PaymentWallet(View):
    def get(self, request) -> object:
        credentials = PaymentWallet.objects.all()
        context = {"credentials": credentials}
        return render(request, 'master_menu/templates/mst_payment_wallets/index.html', context)

    def post(self, request) -> HttpResponse:
        form = MstPaymentWalletForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Credentials created successfully!')
        else:
            return HttpResponseBadRequest(form.errors)

    def put(self, request, pk):
        instance = get_object_or_404(PaymentWallet, pk=pk)
        form = MstPaymentWalletForm(request.PUT, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponse('Credentials updated successfully!')
        else:
            return render(request, 'master_menu/templates/mst_payment_wallets/update.html',
                          {'form': form, 'instance': instance})

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return JsonResponse({'message': 'PaymentWallet credential deleted successfully.'})
