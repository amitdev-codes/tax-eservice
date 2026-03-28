from django.shortcuts import render


def tax_paid(request):
    return render(request, 'payment/templates/tax_paid.html')
