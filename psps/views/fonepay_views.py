from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from psps.models import FonepayWebCredential, VwAppClientModel, PaymentWardModel
from psps.forms import FonepayForm


class FonepayListView(ListView):
    model = FonepayWebCredential
    template_name = 'psps/templates/psp/fonepay/index.html'
    context_object_name = 'credentials'


class FonepayDetailView(DetailView):
    model = FonepayWebCredential
    template_name = 'psps/templates/psp/fonepay/detail.html'
    context_object_name = 'credential'


class FonepayCreateView(CreateView):
    model = FonepayWebCredential
    form_class = FonepayForm
    template_name = 'psps/templates/psp/fonepay/create.html'
    success_url = '/fonepay'  # Redirects to the list view after successful creation

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        clients = VwAppClientModel.objects.values_list('id', 'name_en', 'name_np').order_by('name_en')
        context['clients'] = list(clients)

        wards = PaymentWardModel.objects.values_list('id', 'payment_ward').order_by('id')
        context['wards'] = list(wards)

        return context


class FonepayUpdateView(UpdateView):
    model = FonepayWebCredential
    form_class = FonepayForm
    template_name = 'psps/templates/psp/fonepay/update.html'
    success_url = '/fonepay'  # Redirects to the list view after successful update

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        clients = VwAppClientModel.objects.values_list('id', 'name_en', 'name_np').order_by('name_en')
        context['clients'] = list(clients)
        wards = PaymentWardModel.objects.values_list('id', 'payment_ward').order_by('id')
        context['wards'] = list(wards)

        return context


class FonepayDeleteView(DeleteView):
    model = FonepayWebCredential
    success_url = '/fonepay'


class Fonepay(View):
    def get(self, request):
        credentials = FonepayWebCredential.objects.all()
        context = {"credentials": credentials}

        return render(request, 'psps/templates/psp/fonepay/index.html', context)

    def post(self, request):
        form = FonepayForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Credentials created successfully!')
        else:
            return HttpResponseBadRequest(form.errors)
            # return render(request, 'psps/templates/psp/fonepay/create.html', {'form': form})

    def put(self, request, pk):
        instance = get_object_or_404(FonepayWebCredential, pk=pk)
        form = FonepayForm(request.PUT, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponse('Credentials updated successfully!')
        else:
            return render(request, 'psps/templates/psp/fonepay/update.html',
                          {'form': form, 'instance': instance})

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return JsonResponse({'message': 'Fonepay credential deleted successfully.'})
