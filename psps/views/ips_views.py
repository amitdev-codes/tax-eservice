from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from psps.models import IpsWebCredential, VwAppClientModel, PaymentWardModel
from psps.forms import IpsForm


class IpsListView(ListView):
    model = IpsWebCredential
    template_name = 'psps/templates/psp/ips/index.html'
    context_object_name = 'credentials'


class IpsDetailView(DetailView):
    model = IpsWebCredential
    template_name = 'psps/templates/psp/ips/detail.html'
    context_object_name = 'credential'


class IpsCreateView(CreateView):
    model = IpsWebCredential
    form_class = IpsForm
    template_name = 'psps/templates/psp/ips/create.html'
    success_url = '/ips'  # Redirects to the list view after successful creation

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        clients = VwAppClientModel.objects.values_list('id', 'name_en', 'name_np').order_by('name_en')
        context['clients'] = list(clients)

        wards = PaymentWardModel.objects.values_list('id', 'payment_ward').order_by('id')
        context['wards'] = list(wards)

        return context


class IpsUpdateView(UpdateView):
    model = IpsWebCredential
    form_class = IpsForm
    template_name = 'psps/templates/psp/ips/update.html'
    success_url = '/ips'  # Redirects to the list view after successful update

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        clients = VwAppClientModel.objects.values_list('id', 'name_en', 'name_np').order_by('name_en')
        context['clients'] = list(clients)
        wards = PaymentWardModel.objects.values_list('id', 'payment_ward').order_by('id')
        context['wards'] = list(wards)

        return context


class IpsDeleteView(DeleteView):
    model = IpsWebCredential
    success_url = '/ips'


class Ips(View):
    def get(self, request):
        credentials = IpsWebCredential.objects.all()
        context = {"credentials": credentials}

        return render(request, 'psps/templates/psp/ips/index.html', context)

    def post(self, request):
        form = IpsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Credentials created successfully!')
        else:
            return HttpResponseBadRequest(form.errors)


    def put(self, request, pk):
        instance = get_object_or_404(IpsWebCredential, pk=pk)
        form = IpsForm(request.PUT, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponse('Credentials updated successfully!')
        else:
            return render(request, 'psps/templates/psp/ips/update.html',
                          {'form': form, 'instance': instance})

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return JsonResponse({'message': 'Ips credential deleted successfully.'})
