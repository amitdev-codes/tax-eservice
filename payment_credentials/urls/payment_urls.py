from django.urls import path

from payment_credentials.views.web_payment_log_views import WebPaymentLogListView, WebPaymentLogDetailView, \
    WebPaymentLogCreateView, WebPaymentLogUpdateView, WebPaymentLogDeleteView

urlpatterns = [
    path('', WebPaymentLogListView.as_view(), name='app_client_settings_credential'),
    path('view/<str:pk>/', WebPaymentLogDetailView.as_view(), name='view_app_client_settings_credential'),
    path('update/<str:pk>/', WebPaymentLogUpdateView.as_view(), name='update_app_client_settings_credential'),
    path('delete/<str:pk>/', WebPaymentLogDeleteView.as_view(), name='delete_app_client_settings_credential'),
]
