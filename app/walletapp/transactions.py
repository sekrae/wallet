from django.db import transaction
from walletapp.models import Transaction, Account


class InsufficientFundsException(Exception):
    """Исключение для случаев недостатка средств на счете"""
    pass


class InvalidAmountException(Exception):
    """Исключение для случаев неверной суммы транзакции (0 или меньше)"""
    pass


class SameAccountTransferException(Exception):
    """Исключение для случаев перевода на тот же самый счет"""
    pass



def withdraw(account, amount):
    if amount <= 0:
        raise InvalidAmountException('Сумма транзакции должна быть больше 0')
    with transaction.atomic():
        account = Account.objects.select_for_update().get(account_number=account.account_number)
        if account.current_balance >= amount:
            account.current_balance -= amount
            account.save()
            Transaction.objects.create(
                transaction_type='WITHDRAWAL',
                amount=amount,
                from_account=account
            )
        else:
            raise InsufficientFundsException('Недостаточно средств на счете для снятия')


def transfer(from_account, to_account, amount):
    if amount <= 0:
        raise InvalidAmountException('Сумма транзакции должна быть больше 0')
    if from_account == to_account:
        raise SameAccountTransferException('Невозможно перевести деньги на тот же самый счет')
    with transaction.atomic():
        from_account = Account.objects.select_for_update().get(account_number=from_account.account_number)
        to_account = Account.objects.select_for_update().get(account_number=to_account.account_number)
        if from_account.current_balance >= amount:
            from_account.current_balance -= amount
            to_account.current_balance += amount
            from_account.save()
            to_account.save()
            Transaction.objects.create(
                transaction_type='TRANSFER',
                amount=amount,
                from_account=from_account,
                to_account=to_account
            )
        else:
            raise InsufficientFundsException('Недостаточно средств на счете для перевода')


def deposit(account, amount):
    if amount <= 0:
        raise InvalidAmountException('Сумма транзакции должна быть больше 0')
    with transaction.atomic():
        account = Account.objects.select_for_update().get(account_number=account.account_number)
        account.current_balance += amount
        account.save()
        Transaction.objects.create(
            transaction_type='DEPOSIT',
            amount=amount,
            to_account=account
        )
