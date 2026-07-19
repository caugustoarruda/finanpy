from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from accounts.models import Account
from categories.models import Category
from transactions.forms import TransactionForm
from transactions.models import Transaction


class TransactionListView(LoginRequiredMixin, ListView):
    """List the transactions belonging to the logged-in user.

    Supports filtering through the following query params:
        - ``account``: id of an Account owned by the user.
        - ``category``: id of a Category owned by the user.
        - ``type``: one of ``Transaction.TransactionType`` values
          (``receita``/``despesa``).
        - ``date_from``: minimum ``transaction_date`` (inclusive, ``YYYY-MM-DD``).
        - ``date_to``: maximum ``transaction_date`` (inclusive, ``YYYY-MM-DD``).

    Template context:
        - ``transactions``: the filtered queryset (``context_object_name``).
        - ``account_options``: the user's accounts, to populate the account filter select.
        - ``category_options``: the user's categories, to populate the category filter select.
        - ``type_options``: the ``Transaction.TransactionType`` choices, to populate the type filter select.
        - ``selected_account``, ``selected_category``, ``selected_type``,
          ``selected_date_from``, ``selected_date_to``: the currently applied
          filter values (as submitted, raw strings), so the filter form can
          keep its previous state.
    """

    model = Transaction
    template_name = 'transactions/list.html'
    context_object_name = 'transactions'

    def get_queryset(self):
        queryset = Transaction.objects.filter(user=self.request.user).select_related(
            'account', 'category',
        )

        account_id = self.request.GET.get('account')
        if account_id:
            queryset = queryset.filter(account_id=account_id)

        category_id = self.request.GET.get('category')
        if category_id:
            queryset = queryset.filter(category_id=category_id)

        transaction_type = self.request.GET.get('type')
        if transaction_type:
            queryset = queryset.filter(transaction_type=transaction_type)

        date_from = self.request.GET.get('date_from')
        if date_from:
            queryset = queryset.filter(transaction_date__gte=date_from)

        date_to = self.request.GET.get('date_to')
        if date_to:
            queryset = queryset.filter(transaction_date__lte=date_to)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['account_options'] = Account.objects.filter(user=self.request.user)
        context['category_options'] = Category.objects.filter(user=self.request.user)
        context['type_options'] = Transaction.TransactionType.choices
        context['selected_account'] = self.request.GET.get('account', '')
        context['selected_category'] = self.request.GET.get('category', '')
        context['selected_type'] = self.request.GET.get('type', '')
        context['selected_date_from'] = self.request.GET.get('date_from', '')
        context['selected_date_to'] = self.request.GET.get('date_to', '')
        return context


class TransactionCreateView(LoginRequiredMixin, CreateView):
    """Create a new transaction for the logged-in user."""

    form_class = TransactionForm
    template_name = 'transactions/form.html'
    success_url = reverse_lazy('transactions:list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        response = super().form_valid(form)
        messages.success(self.request, 'Transação criada com sucesso!')
        return response


class TransactionUpdateView(LoginRequiredMixin, UpdateView):
    """Update an existing transaction owned by the logged-in user."""

    form_class = TransactionForm
    template_name = 'transactions/form.html'
    success_url = reverse_lazy('transactions:list')

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Transação atualizada com sucesso!')
        return response


class TransactionDeleteView(LoginRequiredMixin, DeleteView):
    """Delete a transaction owned by the logged-in user."""

    model = Transaction
    template_name = 'transactions/confirm_delete.html'
    success_url = reverse_lazy('transactions:list')

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Transação excluída com sucesso!')
        return response
