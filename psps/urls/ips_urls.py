from django.urls import path
from .. import views
from ..views.ips_views import IpsListView, IpsDetailView, IpsCreateView, IpsUpdateView, IpsDeleteView

urlpatterns = [
    path('', IpsListView.as_view(), name='ips_credential'),
    path('view/<str:pk>/', IpsDetailView.as_view(), name='view_ips_credential'),
    path('create/', IpsCreateView.as_view(), name='create_ips_credential'),
    path('update/<str:pk>/', IpsUpdateView.as_view(), name='update_ips_credential'),
    path('delete/<str:pk>/', IpsDeleteView.as_view(), name='delete_ips_credential'),
]
