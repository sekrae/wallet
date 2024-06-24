from django.db import models
from walletapp.models import Account


class Transaction(models.Model):
    TRANSACTION_TYPE_CHOICES = [
        ('WITHDRAWAL', 'Снятие'),
        ('TRANSFER', 'Перевод'),
        ('DEPOSIT', 'Пополнение')
    ]

    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPE_CHOICES, verbose_name='Тип транзакции')
    amount = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Сумма')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата транзакции')

    from_account = models.ForeignKey(Account, related_name='outgoing_transactions', on_delete=models.CASCADE, null=True, blank=True, verbose_name='С какого счета')
    to_account = models.ForeignKey(Account, related_name='incoming_transactions', on_delete=models.CASCADE, null=True, blank=True, verbose_name='На какой счет')

    class Meta:
        verbose_name = 'Транзакция'
        verbose_name_plural = 'Транзакции'

    def __str__(self):
        return f'{self.transaction_type} - {self.amount}'
