from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from payment_credentials.models import WebPaymentLogModel
from master_menu.models import (AppSettingMaster, VwAppClientwiseSetting, VwMstCountry, \
                                VwAppClient, TaxTypes, MstTaxTypeOnlinePayment)
from payment_credentials.forms import WebPaymentLogForm
from psps.models import VwAppClientModel


class WebPaymentLogListView(ListView):
    model = WebPaymentLogModel
    template_name = 'master_menu/templates/acc_receipt_flag/index.html'
    context_object_name = 'credentials'


class WebPaymentLogDetailView(DetailView):
    model = WebPaymentLogModel
    template_name = 'master_menu/templates/acc_receipt_flag/detail.html'
    context_object_name = 'credential'


class WebPaymentLogCreateView(CreateView):
    model = WebPaymentLogModel
    form_class = WebPaymentLogForm
    template_name = 'master_menu/templates/acc_receipt_flag/create.html'
    success_url = '/client_settings/acc_receipt_flags'  # Redirects to the list view after successful creation

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


class WebPaymentLogUpdateView(UpdateView):
    model = WebPaymentLogModel
    form_class = WebPaymentLogForm
    template_name = 'master_menu/templates/acc_receipt_flag/update.html'
    success_url = '/client_settings/acc_receipt_flags'  # Redirects to the list view after successful update

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        clients = VwAppClientModel.objects.values_list('id', 'name_en', 'name_np').order_by('name_en')
        context['clients'] = list(clients)

        tax_types = TaxTypes.objects.filter(is_deleted=False).values_list('id', 'name_en', 'name_np').order_by(
            'name_en')
        context['tax_types'] = list(tax_types)
        return context


class WebPaymentLogDeleteView(DeleteView):
    model = WebPaymentLogModel
    success_url = '/client_settings/acc_receipt_flags'


class WebPaymentLog(View):
    def get(self, request) -> object:
        credentials = WebPaymentLog.objects.all()
        context = {"credentials": credentials}
        return render(request, 'master_menu/templates/acc_receipt_flag/index.html', context)

    def post(self, request) -> HttpResponse:
        form = WebPaymentLogForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Credentials created successfully!')
        else:
            return HttpResponseBadRequest(form.errors)

    def put(self, request, pk):
        instance = get_object_or_404(WebPaymentLog, pk=pk)
        form = WebPaymentLogForm(request.PUT, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponse('Credentials updated successfully!')
        else:
            return render(request, 'master_menu/templates/acc_receipt_flag/update.html',
                          {'form': form, 'instance': instance})

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return JsonResponse({'message': 'WebPaymentLog credential deleted successfully.'})
