from django.contrib import admin

from transactions.models import Transaction


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    """Admin configuration for the Transaction model."""

    list_display = (
        'description',
        'amount',
        'transaction_type',
        'account',
        'category',
        'transaction_date',
        'user',
    )
    list_filter = ('transaction_type', 'account', 'category')
    search_fields = ('description', 'user__email')
    readonly_fields = ('created_at', 'updated_at')
