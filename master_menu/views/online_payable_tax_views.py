from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from master_menu.models import MstTaxTypeOnlinePayment, AppSettingMaster, VwAppClientwiseSetting, VwMstCountry, \
    VwAppClient, TaxTypes
from master_menu.forms import MstTaxTypeOnlinePaymentForm
from psps.models import VwAppClientModel
from taxeservice.settings import CLIENT_ID


class OnlinePayableTaxListView(ListView):
    model = MstTaxTypeOnlinePayment
    template_name = 'master_menu/templates/online_payable_tax/index.html'
    context_object_name = 'credentials'


class OnlinePayableTaxDetailView(DetailView):
    model = MstTaxTypeOnlinePayment
    template_name = 'master_menu/templates/online_payable_tax/detail.html'
    context_object_name = 'credential'


class OnlinePayableTaxCreateView(CreateView):
    model = MstTaxTypeOnlinePayment
    form_class = MstTaxTypeOnlinePaymentForm
    template_name = 'master_menu/templates/online_payable_tax/create.html'
    success_url = '/client_settings/online_payable_tax'  # Redirects to the list view after successful creation

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        clients = VwAppClientModel.objects.values_list('id', 'name_en', 'name_np').order_by('name_en')
        context['clients'] = list(clients)

        tax_types = TaxTypes.objects.filter(is_deleted=False).values_list('id', 'name_en', 'name_np').order_by(
            'name_en')
        context['tax_types'] = list(tax_types)
        context['client_id'] = CLIENT_ID
        return context


class OnlinePayableTaxUpdateView(UpdateView):
    model = MstTaxTypeOnlinePayment
    form_class = MstTaxTypeOnlinePaymentForm
    template_name = 'master_menu/templates/online_payable_tax/update.html'
    success_url = '/client_settings/online_payable_tax'  # Redirects to the list view after successful update

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        clients = VwAppClientModel.objects.values_list('id', 'name_en', 'name_np').order_by('name_en')
        context['clients'] = list(clients)

        tax_types = TaxTypes.objects.filter(is_deleted=False).values_list('id', 'name_en', 'name_np').order_by(
            'name_en')
        context['tax_types'] = list(tax_types)
        return context


class OnlinePayableTaxDeleteView(DeleteView):
    model = MstTaxTypeOnlinePayment
    success_url = '/client_settings/online_payable_tax'


class OnlinePayableTax(View):
    def get(self, request) -> object:
        credentials = OnlinePayableTax.objects.all()
        context = {"credentials": credentials}
        return render(request, 'master_menu/templates/online_payable_tax/index.html', context)

    def post(self, request) -> HttpResponse:
        form = MstTaxTypeOnlinePaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Credentials created successfully!')
        else:
            return HttpResponseBadRequest(form.errors)

    def put(self, request, pk):
        instance = get_object_or_404(OnlinePayableTax, pk=pk)
        form = MstTaxTypeOnlinePaymentForm(request.PUT, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponse('Credentials updated successfully!')
        else:
            return render(request, 'master_menu/templates/online_payable_tax/update.html',
                          {'form': form, 'instance': instance})

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return JsonResponse({'message': 'OnlinePayableTax credential deleted successfully.'})


