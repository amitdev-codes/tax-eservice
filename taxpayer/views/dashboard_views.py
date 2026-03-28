from django.shortcuts import render


def dashboard(request):
    return render(request, 'taxpayer/templates/dashboard.html')
