from django.urls import path

from . import views
from .views import ATMWithdrawalView

urlpatterns = [
    path('view1/', views.view1, name='view1'),
    path('view2/', views.view2, name='view2'),
    path('view3/', views.view3, name='view3'),
    path('withdrawal/', ATMWithdrawalView.as_view(), name='atm-withdrawal'),
]