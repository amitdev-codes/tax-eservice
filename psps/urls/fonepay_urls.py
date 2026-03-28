from django.urls import path
from .. import views
from ..views.fonepay_views import FonepayListView, FonepayDetailView, FonepayCreateView, FonepayUpdateView, FonepayDeleteView

urlpatterns = [
    path('', FonepayListView.as_view(), name='fonepay_credential'),
    path('view/<str:pk>/', FonepayDetailView.as_view(), name='view_fonepay_credential'),
    path('create/', FonepayCreateView.as_view(), name='create_fonepay_credential'),
    path('update/<str:pk>/', FonepayUpdateView.as_view(), name='update_fonepay_credential'),
    path('delete/<str:pk>/', FonepayDeleteView.as_view(), name='delete_fonepay_credential'),
]
