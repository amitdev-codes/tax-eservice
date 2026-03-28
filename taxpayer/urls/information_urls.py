from django.urls import path

from ..views import information_views
from ..views import dashboard_views


urlpatterns = [
    path('dashboard', dashboard_views.dashboard, name='user_dashboard'),
    path('personal', information_views.personal, name='personal_details')
]
