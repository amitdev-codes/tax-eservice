from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('master_menu.urls.app_client_settings_urls'))
]
