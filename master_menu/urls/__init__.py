from django.urls import path, include

urlpatterns = [
    path('client_settings/', include('master_menu.urls.app_client_settings_urls')),
]
