from django.conf import settings
from django.db import models

from core.models import TimeStampedModel


class Category(TimeStampedModel):
    """An income or expense category owned by a User, used to classify transactions."""

    class CategoryType(models.TextChoices):
        RECEITA = 'receita', 'Receita'
        DESPESA = 'despesa', 'Despesa'

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='categories',
    )
    name = models.CharField('Nome', max_length=100)
    category_type = models.CharField(
        'Tipo',
        max_length=20,
        choices=CategoryType.choices,
    )
    color = models.CharField('Cor', max_length=7, default='#6366f1')

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return f'{self.name} ({self.user.email})'
