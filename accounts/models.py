from django.conf import settings
from django.db import models

from core.models import TimeStampedModel


class Account(TimeStampedModel):
    """A bank account (or similar money holder) owned by a User."""

    class AccountType(models.TextChoices):
        WALLET = 'wallet', 'Carteira'
        CHECKING = 'checking', 'Conta corrente'
        SAVINGS = 'savings', 'Poupança'
        INVESTMENT = 'investment', 'Investimento'
        CREDIT_CARD = 'credit_card', 'Cartão de crédito'

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='accounts',
    )
    name = models.CharField('Nome', max_length=100)
    account_type = models.CharField(
        'Tipo de conta',
        max_length=20,
        choices=AccountType.choices,
    )
    initial_balance = models.DecimalField(
        'Saldo inicial',
        max_digits=12,
        decimal_places=2,
        default=0,
    )

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return f'{self.name} ({self.user.email})'
