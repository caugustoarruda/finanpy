from decimal import Decimal

from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models

from core.models import TimeStampedModel


class Transaction(TimeStampedModel):
    """A financial transaction (income or expense) owned by a User."""

    class TransactionType(models.TextChoices):
        RECEITA = 'receita', 'Receita'
        DESPESA = 'despesa', 'Despesa'

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='transactions',
    )
    account = models.ForeignKey(
        'accounts.Account',
        on_delete=models.CASCADE,
        related_name='transactions',
        verbose_name='Conta',
    )
    category = models.ForeignKey(
        'categories.Category',
        on_delete=models.CASCADE,
        related_name='transactions',
        verbose_name='Categoria',
    )
    description = models.CharField('Descrição', max_length=255, blank=True)
    amount = models.DecimalField(
        'Valor',
        max_digits=12,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'), message='O valor deve ser maior que zero.')],
    )
    transaction_type = models.CharField(
        'Tipo',
        max_length=20,
        choices=TransactionType.choices,
    )
    transaction_date = models.DateField('Data')

    class Meta:
        ordering = ('-transaction_date', '-created_at')

    def __str__(self):
        return f'{self.description or self.get_transaction_type_display()} - {self.amount} ({self.user.email})'
