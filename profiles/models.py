from django.conf import settings
from django.db import models

from core.models import TimeStampedModel


class Profile(TimeStampedModel):
    """Complementary profile data for a User."""

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='profile',
    )
    phone = models.CharField('Telefone', max_length=20, blank=True)
    birth_date = models.DateField('Data de nascimento', null=True, blank=True)
    avatar = models.URLField('Avatar', blank=True)

    def __str__(self):
        return f'Perfil de {self.user.email}'
