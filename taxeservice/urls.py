"""
URL configuration for taxeservice project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.shortcuts import render, redirect
from django.urls import path, include
from django.utils.translation import activate

from psps import urls


# def languagechange(request):
#     language = request.GET.get('language')
#
#     if language:
#         activate(language)
#         request.session['language'] = language
#
#         # If language is not provided in the query parameter, check if it's stored in the session
#     else:
#         language = request.session.get('language')
#         if language:
#             activate(language)
#         else:
#             # Default language
#             activate('ne')
#
#     return render(request, "authentication/templates/login.html")


def localization(request):
    language = request.GET.get('language')
    if language:
        activate(language)
        request.session['language'] = language
    else:
        language = request.session.get('language')
        if language:
            activate(language)
        else:
            # Default language
            activate('ne')

    next_page = request.META.get('HTTP_REFERER', '/')
    return redirect(next_page)


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('/localization', localization, name='localization'),
    path('', include('authentication.urls')),
    path('', include('taxpayer.urls')),
    path('', include('psps.urls')),
    path('', include('master_menu.urls')),
    path('', include('payment_credentials.urls')),
    path('', include('payment.urls')),
]
