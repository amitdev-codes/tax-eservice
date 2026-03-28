from django.urls import path
from .. import views
from ..views.esewa_views import EsewaListView, EsewaDetailView, EsewaCreateView, EsewaUpdateView, EsewaDeleteView

urlpatterns = [
    path('', EsewaListView.as_view(), name='esewa_credential'),
    path('view/<str:pk>/', EsewaDetailView.as_view(), name='view_esewa_credential'),
    path('create/', EsewaCreateView.as_view(), name='create_esewa_credential'),
    path('update/<str:pk>/', EsewaUpdateView.as_view(), name='update_esewa_credential'),
    path('delete/<str:pk>/', EsewaDeleteView.as_view(), name='delete_esewa_credential'),
]
