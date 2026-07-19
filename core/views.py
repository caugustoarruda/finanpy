from decimal import Decimal

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.db.models.functions import Coalesce
from django.shortcuts import redirect
from django.utils import timezone
from django.views.generic import TemplateView

from accounts.models import Account
from transactions.models import Transaction


class LandingPageView(TemplateView):
    """Public landing page, redirects authenticated users to the dashboard."""

    template_name = 'core/landing.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        return super().dispatch(request, *args, **kwargs)


class DashboardView(LoginRequiredMixin, TemplateView):
    """Authenticated user's financial overview."""

    template_name = 'core/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        contas_saldo = Account.objects.filter(user=user).aggregate(
            total=Coalesce(Sum('initial_balance'), Decimal('0'))
        )['total']

        receitas_total = Transaction.objects.filter(
            user=user, transaction_type=Transaction.TransactionType.RECEITA
        ).aggregate(total=Coalesce(Sum('amount'), Decimal('0')))['total']

        despesas_total = Transaction.objects.filter(
            user=user, transaction_type=Transaction.TransactionType.DESPESA
        ).aggregate(total=Coalesce(Sum('amount'), Decimal('0')))['total']

        saldo_total = contas_saldo + receitas_total - despesas_total

        now = timezone.now()

        receitas_mes = Transaction.objects.filter(
            user=user,
            transaction_type=Transaction.TransactionType.RECEITA,
            transaction_date__year=now.year,
            transaction_date__month=now.month,
        ).aggregate(total=Coalesce(Sum('amount'), Decimal('0')))['total']

        despesas_mes = Transaction.objects.filter(
            user=user,
            transaction_type=Transaction.TransactionType.DESPESA,
            transaction_date__year=now.year,
            transaction_date__month=now.month,
        ).aggregate(total=Coalesce(Sum('amount'), Decimal('0')))['total']

        ultimas_transacoes = Transaction.objects.filter(user=user).select_related(
            'account', 'category'
        )[:5]

        context.update({
            'saldo_total': saldo_total,
            'receitas_mes': receitas_mes,
            'despesas_mes': despesas_mes,
            'ultimas_transacoes': ultimas_transacoes,
        })
        return context
