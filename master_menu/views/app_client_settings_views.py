from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from master_menu.models import AppClientSettingModel, AppSettingMaster, VwAppClientwiseSetting, VwMstCountry, \
    VwAppClient
from master_menu.forms import AppClientSettingForm
from psps.models import VwAppClientModel


class AppClientSettingListView(ListView):
    model = AppClientSettingModel
    template_name = 'master_menu/templates/app_client_settings/index.html'
    context_object_name = 'credentials'


class AppClientSettingDetailView(DetailView):
    model = AppClientSettingModel
    template_name = 'master_menu/templates/app_client_settings/detail.html'
    context_object_name = 'credential'


class AppClientSettingCreateView(CreateView):
    model = AppClientSettingModel
    form_class = AppClientSettingForm
    template_name = 'master_menu/templates/app_client_settings/create.html'
    success_url = '/client_settings/'  # Redirects to the list view after successful creation

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        clients = VwAppClientModel.objects.values_list('id', 'name_en', 'name_np').order_by('name_en')
        context['clients'] = list(clients)
        return context


class AppClientSettingUpdateView(UpdateView):
    model = AppClientSettingModel
    form_class = AppClientSettingForm
    template_name = 'master_menu/templates/app_client_settings/update.html'
    success_url = '/client_settings/'  # Redirects to the list view after successful update

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        clients = VwAppClientModel.objects.values_list('id', 'name_en', 'name_np').order_by('name_en')
        context['clients'] = list(clients)
        return context


class AppClientSettingDeleteView(DeleteView):
    model = AppClientSettingModel
    success_url = '/client_settings/'


class AppClientSetting(View):
    def get(self, request) -> object:
        credentials = AppClientSettingModel.objects.all()
        context = {"credentials": credentials}
        return render(request, 'master_menu/templates/app_client_settings/index.html', context)

    def post(self, request)->HttpResponse:
        form = AppClientSettingForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Credentials created successfully!')
        else:
            return HttpResponseBadRequest(form.errors)

    def put(self, request, pk):
        instance = get_object_or_404(AppClientSettingModel, pk=pk)
        form = AppClientSettingForm(request.PUT, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponse('Credentials updated successfully!')
        else:
            return render(request, 'master_menu/templates/app_client_settings/update.html',
                          {'form': form, 'instance': instance})

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return JsonResponse({'message': 'AppClientSetting credential deleted successfully.'})


def fetch_credentials(request):
    if request.method == 'GET':

        client_id = request.GET.get('client_id')
        code = 'mun_vdc_id'
        country_id = 105
        setting_id = AppSettingMaster.objects.filter(code=code).values_list('id', flat=True).first()
        country = VwMstCountry.objects.filter(id=country_id).values_list('name_np', flat=True).first()

        query = """
             SELECT
             1 as id,
         		CONCAT_WS('',mfhpk.name_np,'-',mfhp.name_np,
				 '-',%s)as address
         	FROM
         		vw_app_clientwise_setting as c
         		LEFT JOIN vw_mst_federal_hierarchy mfh ON mfh.ID = c.combo_value
         		LEFT JOIN vw_mst_federal_hierarchy mfhp ON mfhp.ID = mfh.parent_id
         		LEFT JOIN vw_mst_federal_hierarchy mfhpk ON mfhpk.ID = mfhp.parent_id
         	WHERE
         		c.setting_id = %s
         		AND c.client_id =%s
           """
        client_wise_settings = VwAppClientwiseSetting.objects.raw(query, [country, setting_id, client_id])
        for setting in client_wise_settings:
            address = setting.address

        client_name = VwAppClient.objects.filter(id=client_id).values_list('name_np', flat=True).first()
        cfy = AppSettingMaster.objects.filter(code='CURRENTFISCALYEAR').values_list('id', flat=True).first()
        rid = AppSettingMaster.objects.filter(code='muntax_receipt_type').values_list('id', flat=True).first()
        cyr_id = AppSettingMaster.objects.filter(code='DEFAULT_PROPERTY_ACCOUNTID').values_list('id', flat=True).first()
        pyr_id = AppSettingMaster.objects.filter(code='PREVIOUS_UNPAID_IPT_ACCOUNTID').values_list('id',
                                                                                                   flat=True).first()
        fiscal_year = VwAppClientwiseSetting.objects.filter(setting_id=cfy, client_id=client_id).values('default_value',
                                                                                                        'combo_value').first()
        last_fiscal_year = fiscal_year['default_value'].split('/')[-1]
        receipt_type = VwAppClientwiseSetting.objects.filter(setting_id=rid,
                                                             client_id=client_id).values('default_value',
                                                                                         'combo_value').first()

        cyr = VwAppClientwiseSetting.objects.filter(setting_id=cyr_id,
                                                    client_id=client_id).values('default_value', 'combo_value').first()
        pyr = VwAppClientwiseSetting.objects.filter(setting_id=pyr_id,
                                                    client_id=client_id).values('default_value', 'combo_value').first()

        lm = AppSettingMaster.objects.filter(code='LANDMEASURINGUNIT').values_list('id', flat=True).first()
        land_measuring_unit = VwAppClientwiseSetting.objects.filter(setting_id=lm, client_id=client_id).values(
            'default_value',
            'combo_value').first()

        lu = AppSettingMaster.objects.filter(code='SPACEMEASURINGUNIT').values_list('id', flat=True).first()
        length_unit = VwAppClientwiseSetting.objects.filter(setting_id=lu, client_id=client_id).values('default_value',
                                                                                                       'combo_value').first()
        cset_id = AppSettingMaster.objects.filter(code='OFFICE_NAME').values_list('id', flat=True).first()
        client_username = VwAppClientwiseSetting.objects.filter(setting_id=cset_id, client_id=client_id).values_list(
            'default_value', flat=True).first()

        house_land_setting_id = (AppSettingMaster.objects.filter(code='IsHouseLandTaxImplemented')
                                 .values_list('id', flat=True).first())
        hlt_tax_type = VwAppClientwiseSetting.objects.filter(setting_id=house_land_setting_id,
                                                             client_id=client_id).values_list('default_value',
                                                                                              flat=True).first()

        house_land_type = 1 if hlt_tax_type == True else 0

        amount_to = AppSettingMaster.objects.filter(code='tax_amount_to').values_list('default_value',
                                                                                      flat=True).first()
        amount_from = AppSettingMaster.objects.filter(code='tax_amount_from').values_list('default_value',
                                                                                          flat=True).first()

        data = {
            'client_address': address,
            'client_name': client_name,
            'current_fiscal_year_id': fiscal_year['combo_value'],
            'current_fiscal_year_code': fiscal_year['default_value'],
            'last_fiscal_year': last_fiscal_year,
            'receipt_type': receipt_type['default_value'],
            'receipt_value': receipt_type['combo_value'],
            'current_year_rate_id': cyr['default_value'],
            'current_year_rate_value': cyr['combo_value'],
            'previous_year_rate_id': pyr['default_value'],
            'previous_year_rate_value': pyr['combo_value'],
            'land_measuring_id': lm,
            'land_measuring_unit': land_measuring_unit['combo_value'],
            'land_measuring_unit_name': land_measuring_unit['default_value'],
            'length_id': lu,
            'length_unit': length_unit['combo_value'],
            'length_unit_name': length_unit['default_value'],
            'client_username': client_username,
            'is_house_land_tax_implemented': house_land_type,
            'tax_amount_to': amount_to,
            'tax_amount_from': amount_from,
            'is_ebps': 0,
            'is_active': 0,
            'is_ward_wise_psp_mode': 0,
        }
        return JsonResponse(data)
    else:
        return JsonResponse({'error': 'Invalid request'})
