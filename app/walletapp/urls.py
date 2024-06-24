from django.urls import path
from .views import WithdrawView, TransferView, DepositView

urlpatterns = [
    path('withdraw/', WithdrawView.as_view(), name='withdraw'),
    path('transfer/', TransferView.as_view(), name='transfer'),
    path('deposit/', DepositView.as_view(), name='deposit'),
]