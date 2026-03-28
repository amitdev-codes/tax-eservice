from django.urls import path
from .. import views
from ..views.khalti_views import KhaltiListView, KhaltiDetailView, KhaltiCreateView, KhaltiUpdateView, KhaltiDeleteView

urlpatterns = [
    path('', KhaltiListView.as_view(), name='khalti_credential'),
    path('view/<str:pk>/', KhaltiDetailView.as_view(), name='view_khalti_credential'),
    path('create/', KhaltiCreateView.as_view(), name='create_khalti_credential'),
    path('update/<str:pk>/', KhaltiUpdateView.as_view(), name='update_khalti_credential'),
    path('delete/<str:pk>/', KhaltiDeleteView.as_view(), name='delete_khalti_credential'),
]
