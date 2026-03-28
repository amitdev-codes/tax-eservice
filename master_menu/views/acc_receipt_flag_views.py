from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from master_menu.models import AccReceiptFlagModel, AppSettingMaster, VwAppClientwiseSetting, VwMstCountry, \
    VwAppClient, TaxTypes, MstTaxTypeOnlinePayment
from master_menu.forms import AccReceiptFlagForm
from psps.models import VwAppClientModel


class AccReceiptFlagListView(ListView):
    model = AccReceiptFlagModel
    template_name = 'master_menu/templates/acc_receipt_flag/index.html'
    context_object_name = 'credentials'


class AccReceiptFlagDetailView(DetailView):
    model = AccReceiptFlagModel
    template_name = 'master_menu/templates/acc_receipt_flag/detail.html'
    context_object_name = 'credential'


class AccReceiptFlagCreateView(CreateView):
    model = AccReceiptFlagModel
    form_class = AccReceiptFlagForm
    template_name = 'master_menu/templates/acc_receipt_flag/create.html'
    success_url = '/client_settings/acc_receipt_flags'  # Redirects to the list view after successful creation

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        clients = VwAppClientModel.objects.values_list('id', 'name_en', 'name_np').order_by('name_en')
        context['clients'] = list(clients)

        online_payable_taxes = MstTaxTypeOnlinePayment.objects.filter(is_active=True).values_list('tax_type_id',flat=True)
        online_payable_taxes = list(online_payable_taxes)
        tax_types = TaxTypes.objects.filter(id__in=online_payable_taxes, is_deleted=False).values_list('id', 'name_en',
                                                                                                      'name_np').order_by(
            'name_en')
        context['tax_types'] = list(tax_types)
        return context


class AccReceiptFlagUpdateView(UpdateView):
    model = AccReceiptFlagModel
    form_class = AccReceiptFlagForm
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


class AccReceiptFlagDeleteView(DeleteView):
    model = AccReceiptFlagModel
    success_url = '/client_settings/acc_receipt_flags'


class AccReceiptFlag(View):
    def get(self, request) -> object:
        credentials = AccReceiptFlag.objects.all()
        context = {"credentials": credentials}
        return render(request, 'master_menu/templates/acc_receipt_flag/index.html', context)

    def post(self, request) -> HttpResponse:
        form = AccReceiptFlagForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Credentials created successfully!')
        else:
            return HttpResponseBadRequest(form.errors)

    def put(self, request, pk):
        instance = get_object_or_404(AccReceiptFlag, pk=pk)
        form = AccReceiptFlagForm(request.PUT, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponse('Credentials updated successfully!')
        else:
            return render(request, 'master_menu/templates/acc_receipt_flag/update.html',
                          {'form': form, 'instance': instance})

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return JsonResponse({'message': 'AccReceiptFlag credential deleted successfully.'})

