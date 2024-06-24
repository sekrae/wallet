from django.db import models
from walletapp.models import Customer


class Account(models.Model):
    account_name = models.CharField(max_length=255, verbose_name='Название счета')
    account_number = models.CharField(max_length=16, primary_key=True, verbose_name='Номер счета')
    open_date = models.DateField(verbose_name='Дата открытия счета')
    end_date = models.DateField(verbose_name='Дата окончания счета')
    close_date = models.DateField(verbose_name='Дата фактического закрытия счета', null=True, blank=True)

    customer = models.ForeignKey(Customer, verbose_name='Клиент', related_name='accounts', on_delete=models.CASCADE)
    current_balance = models.DecimalField(verbose_name='Текущий баланс', max_digits=20, decimal_places=2,
                                          blank=True, default=0)

    def __str__(self):
        return f'{self.account_number} - {self.account_name}'

    class Meta:
        verbose_name = 'Счёт'
        verbose_name_plural = 'Счета'

    def get_status(self):
        return 'Закрыт' if self.close_date else 'Активен'
