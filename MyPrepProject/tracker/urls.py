from django.urls import path
from . import views

urlpatterns = [
    path('checkin/', views.check_in, name='check_in'),
    path('checkout/', views.check_out, name='check_out'),
    path('', views.dashboard, name='dashboard'),
]