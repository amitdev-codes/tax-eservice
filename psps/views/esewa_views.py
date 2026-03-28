from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from psps.models import EsewaWebCredential, VwAppClientModel, PaymentWardModel
from psps.forms import EsewaForm


class EsewaListView(ListView):
    model = EsewaWebCredential
    template_name = 'psps/templates/psp/esewa/index.html'
    context_object_name = 'credentials'


class EsewaDetailView(DetailView):
    model = EsewaWebCredential
    template_name = 'psps/templates/psp/esewa/detail.html'
    context_object_name = 'credential'


class EsewaCreateView(CreateView):
    model = EsewaWebCredential
    form_class = EsewaForm
    template_name = 'psps/templates/psp/esewa/create.html'
    success_url = '/esewa'  # Redirects to the list view after successful creation

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        clients = VwAppClientModel.objects.values_list('id', 'name_en', 'name_np').order_by('name_en')
        context['clients'] = list(clients)

        wards = PaymentWardModel.objects.values_list('id', 'payment_ward').order_by('id')
        context['wards'] = list(wards)

        return context


class EsewaUpdateView(UpdateView):
    model = EsewaWebCredential
    form_class = EsewaForm
    template_name = 'psps/templates/psp/esewa/update.html'
    success_url = '/esewa'  # Redirects to the list view after successful update

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        clients = VwAppClientModel.objects.values_list('id', 'name_en', 'name_np').order_by('name_en')
        context['clients'] = list(clients)
        wards = PaymentWardModel.objects.values_list('id', 'payment_ward').order_by('id')
        context['wards'] = list(wards)

        return context


class EsewaDeleteView(DeleteView):
    model = EsewaWebCredential
    success_url = '/esewa'


class Esewa(View):
    def get(self, request):
        credentials = EsewaWebCredential.objects.all()
        context = {"credentials": credentials}

        return render(request, 'psps/templates/psp/esewa/index.html', context)

    def post(self, request):
        form = EsewaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Credentials created successfully!')
        else:
            return HttpResponseBadRequest(form.errors)
            # return render(request, 'psps/templates/psp/esewa/create.html', {'form': form})

    def put(self, request, pk):
        instance = get_object_or_404(EsewaWebCredential, pk=pk)
        form = EsewaForm(request.PUT, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponse('Credentials updated successfully!')
        else:
            return render(request, 'psps/templates/psp/esewa/update.html',
                          {'form': form, 'instance': instance})

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return JsonResponse({'message': 'Esewa credential deleted successfully.'})
