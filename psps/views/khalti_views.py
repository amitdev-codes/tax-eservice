from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from psps.models import KhaltiWebCredential, VwAppClientModel, PaymentWardModel
from psps.forms import KhaltiForm


class KhaltiListView(ListView):
    model = KhaltiWebCredential
    template_name = 'psps/templates/psp/khalti/index.html'
    context_object_name = 'credentials'


class KhaltiDetailView(DetailView):
    model = KhaltiWebCredential
    template_name = 'psps/templates/psp/khalti/detail.html'
    context_object_name = 'credential'


class KhaltiCreateView(CreateView):
    model = KhaltiWebCredential
    form_class = KhaltiForm
    template_name = 'psps/templates/psp/khalti/create.html'
    success_url = '/khalti'  # Redirects to the list view after successful creation

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        clients = VwAppClientModel.objects.values_list('id', 'name_en', 'name_np').order_by('name_en')
        context['clients'] = list(clients)

        wards = PaymentWardModel.objects.values_list('id', 'payment_ward').order_by('id')
        context['wards'] = list(wards)

        return context


class KhaltiUpdateView(UpdateView):
    model = KhaltiWebCredential
    form_class = KhaltiForm
    template_name = 'psps/templates/psp/khalti/update.html'
    success_url = '/khalti'  # Redirects to the list view after successful update

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        clients = VwAppClientModel.objects.values_list('id', 'name_en', 'name_np').order_by('name_en')
        context['clients'] = list(clients)
        wards = PaymentWardModel.objects.values_list('id', 'payment_ward').order_by('id')
        context['wards'] = list(wards)

        return context


class KhaltiDeleteView(DeleteView):
    model = KhaltiWebCredential
    success_url = '/khalti'


class Khalti(View):
    def get(self, request):
        credentials = KhaltiWebCredential.objects.all()
        context = {"credentials": credentials}

        return render(request, 'psps/templates/psp/khalti/index.html', context)

    def post(self, request):
        form = KhaltiForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Credentials created successfully!')
        else:
            return HttpResponseBadRequest(form.errors)

    def put(self, request, pk):
        instance = get_object_or_404(KhaltiWebCredential, pk=pk)
        form = KhaltiForm(request.PUT, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponse('Credentials updated successfully!')
        else:
            return render(request, 'psps/templates/psp/khalti/update.html',
                          {'form': form, 'instance': instance})

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return JsonResponse({'message': 'Khalti credential deleted successfully.'})
