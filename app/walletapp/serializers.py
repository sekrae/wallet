from rest_framework import serializers
from .models import Account, Transaction


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'


class WithdrawSerializer(serializers.Serializer):
    account_number = serializers.CharField(max_length=16, help_text='Номер счета')
    amount = serializers.DecimalField(max_digits=20, decimal_places=2, help_text='Сумма снятия')


class TransferSerializer(serializers.Serializer):
    from_account_number = serializers.CharField(max_length=16, help_text='Номер счета отправителя')
    to_account_number = serializers.CharField(max_length=16, help_text='Номер счета получателя')
    amount = serializers.DecimalField(max_digits=20, decimal_places=2, help_text='Сумма перевода')


class DepositSerializer(serializers.Serializer):
    account_number = serializers.CharField(max_length=16, help_text='Номер счета')
    amount = serializers.DecimalField(max_digits=20, decimal_places=2, help_text='Сумма пополнения')
