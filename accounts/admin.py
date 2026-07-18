from django.contrib import admin

from accounts.models import Account


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    """Admin configuration for the Account model."""

    list_display = ('name', 'account_type', 'user', 'initial_balance')
    list_filter = ('account_type',)
    search_fields = ('name', 'user__email')
    readonly_fields = ('created_at', 'updated_at')
