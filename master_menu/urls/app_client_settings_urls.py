from django.urls import path
from .. import views
from ..views.acc_receipt_flag_views import AccReceiptFlagListView, AccReceiptFlagDetailView, AccReceiptFlagUpdateView, \
    AccReceiptFlagCreateView, AccReceiptFlagDeleteView
from ..views.app_client_settings_views import AppClientSettingListView, AppClientSettingDetailView, \
    AppClientSettingCreateView, AppClientSettingUpdateView, AppClientSettingDeleteView

from ..views.app_client_settings_views import fetch_credentials
from ..views.mst_payment_wallet_views import PaymentWalletListView, PaymentWalletDetailView, PaymentWalletCreateView, \
    PaymentWalletUpdateView, PaymentWalletDeleteView
from ..views.online_payable_tax_views import OnlinePayableTaxListView, OnlinePayableTaxDetailView, \
    OnlinePayableTaxCreateView, OnlinePayableTaxUpdateView, OnlinePayableTaxDeleteView

urlpatterns = [
    path('', AppClientSettingListView.as_view(), name='app_client_settings_credential'),
    path('view/<str:pk>/', AppClientSettingDetailView.as_view(), name='view_app_client_settings_credential'),
    path('create/', AppClientSettingCreateView.as_view(), name='create_app_client_settings_credential'),
    path('update/<str:pk>/', AppClientSettingUpdateView.as_view(), name='update_app_client_settings_credential'),
    path('delete/<str:pk>/', AppClientSettingDeleteView.as_view(), name='delete_app_client_settings_credential'),
    path('/fetch_credentials/', fetch_credentials, name='fetch_app_client_settings_credential'),

    # Online Payable tax
    path('online_payable_tax', OnlinePayableTaxListView.as_view(), name='online_payable_tax_credential'),
    path('online_payable_taxs/view/<str:pk>/', OnlinePayableTaxDetailView.as_view(),
         name='view_online_payable_tax_credential'),
    path('online_payable_taxs/create/', OnlinePayableTaxCreateView.as_view(),
         name='create_online_payable_tax_credential'),
    path('online_payable_taxs/update/<str:pk>/', OnlinePayableTaxUpdateView.as_view(),
         name='update_online_payable_tax_credential'),
    path('online_payable_taxs/delete/<str:pk>/', OnlinePayableTaxDeleteView.as_view(),
         name='delete_online_payable_tax_credential'),

    # acc receipt flag
    path('acc_receipt_flags', AccReceiptFlagListView.as_view(), name='acc_receipt_flag_credential'),
    path('acc_receipt_flags/view/<str:pk>/', AccReceiptFlagDetailView.as_view(),
         name='view_acc_receipt_flag_credential'),
    path('acc_receipt_flags/create/', AccReceiptFlagCreateView.as_view(), name='create_acc_receipt_flag_credential'),
    path('acc_receipt_flags/update/<str:pk>/', AccReceiptFlagUpdateView.as_view(),
         name='update_acc_receipt_flag_credential'),
    path('acc_receipt_flags/delete/<str:pk>/', AccReceiptFlagDeleteView.as_view(),
         name='delete_acc_receipt_flag_credential'),

    # payment wallets
    path('mst_payment_wallets', PaymentWalletListView.as_view(), name='mst_payment_wallets_credential'),
    path('mst_payment_wallets/view/<str:pk>/', PaymentWalletDetailView.as_view(),
         name='view_mst_payment_wallets_credential'),
    path('mst_payment_wallets/create/', PaymentWalletCreateView.as_view(),
         name='create_mst_payment_wallets_credential'),
    path('mst_payment_wallets/update/<str:pk>/', PaymentWalletUpdateView.as_view(),
         name='update_mst_payment_wallets_credential'),
    path('mst_payment_wallets/delete/<str:pk>/', PaymentWalletDeleteView.as_view(),
         name='delete_mst_payment_wallets_credential'),

]
