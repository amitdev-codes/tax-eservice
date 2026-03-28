from django.urls import path
from . import views

urlpatterns = [
    path('taxpayer', views.list_taxpayer, name='taxpayer'),
    path('create_taxpayer', views.create_taxpayer, name='create_taxpayer'),
    path('update_taxpayer/<str:pk>/', views.update_taxpayer, name='update_taxpayer'),
    path('delete_taxpayer/<str:pk>/', views.delete_taxpayer, name='delete_taxpayer'),
]
