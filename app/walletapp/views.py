from rest_framework import status, views
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from walletapp.models import Account
from .serializers import WithdrawSerializer, TransferSerializer, DepositSerializer
from .transactions import withdraw, transfer, deposit, InsufficientFundsException, InvalidAmountException, \
    SameAccountTransferException

import logging

logger = logging.getLogger(__name__)


class WithdrawView(views.APIView):
    """
    Представление для снятия средств
    """
    def post(self, request, *args, **kwargs):
        serializer = WithdrawSerializer(data=request.data)
        if serializer.is_valid():
            account_number = serializer.validated_data['account_number']
            amount = serializer.validated_data['amount']

            account = get_object_or_404(Account, account_number=account_number)
            try:
                withdraw(account, amount)
                return Response({'status': 'success', 'message': 'Withdrawal successful'}, status=status.HTTP_200_OK)
            except (InsufficientFundsException, InvalidAmountException) as e:
                logger.error("Transaction error: %s", str(e))
                return Response({'status': 'error', 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TransferView(views.APIView):
    """
    Представление для перевода средств
    """
    def post(self, request, *args, **kwargs):
        serializer = TransferSerializer(data=request.data)
        if serializer.is_valid():
            from_account_number = serializer.validated_data['from_account_number']
            to_account_number = serializer.validated_data['to_account_number']
            amount = serializer.validated_data['amount']

            from_account = get_object_or_404(Account, account_number=from_account_number)
            to_account = get_object_or_404(Account, account_number=to_account_number)
            try:
                transfer(from_account, to_account, amount)
                return Response({'status': 'success', 'message': 'Transfer successful'}, status=status.HTTP_200_OK)
            except (InsufficientFundsException, InvalidAmountException, SameAccountTransferException) as e:
                return Response({'status': 'error', 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DepositView(views.APIView):
    """
    Представление для пополнения счета
    """
    def post(self, request, *args, **kwargs):
        serializer = DepositSerializer(data=request.data)
        if serializer.is_valid():
            account_number = serializer.validated_data['account_number']
            amount = serializer.validated_data['amount']

            account = get_object_or_404(Account, account_number=account_number)
            try:
                deposit(account, amount)
                return Response({'status': 'success', 'message': 'Deposit successful'}, status=status.HTTP_200_OK)
            except InvalidAmountException as e:
                return Response({'status': 'error', 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
