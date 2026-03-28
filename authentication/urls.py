from django.urls import path

from . import views


urlpatterns = [
    path('', views.login, name='index'),
    path('authenticate', views.authenticate, name='authenticate'),
    path('logout/', views.handle_logout, name='handle_logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
]
