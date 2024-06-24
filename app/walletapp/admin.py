from django.contrib import admin

from walletapp.models import Account, Transaction, Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'fullname', 'email')
    list_filter = ('fullname', )
    search_fields = ('fullname', 'email')


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('account_name', 'account_number', 'get_fullname', 'current_balance')
    list_filter = ('account_name', 'current_balance')
    search_fields = ('account_name', 'account_number', 'customer__fullname')

    def get_fullname(self, obj):
        return obj.customer.fullname

    get_fullname.admin_order_field = 'customer__fullname'
    get_fullname.short_description = 'ФИО'


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('transaction_type', 'amount', 'from_account', 'to_account', 'date')
    list_filter = ('transaction_type', 'date')
    search_fields = ('from_account__account_number', 'to_account__account_number')

    def get_from_account(self, obj):
        return obj.from_account.account_number

    def get_to_account(self, obj):
        return obj.to_account.account_number

    get_from_account.admin_order_field = 'from_account__account_number'
    get_to_account.admin_order_field = 'to_account__account_number'

