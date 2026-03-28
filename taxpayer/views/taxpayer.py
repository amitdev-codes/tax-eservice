from django.shortcuts import render


def list_taxpayer(request):
    return render(request, "taxpayer/index.html")
