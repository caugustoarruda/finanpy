from django import forms

from accounts.models import Account
from categories.models import Category
from transactions.models import Transaction

INPUT_CLASSES = (
    'w-full rounded-lg border border-slate-300 px-3 py-2 text-sm text-slate-800 '
    'focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent'
)


class OwnedModelChoiceField(forms.ModelChoiceField):
    """ModelChoiceField that displays only the object's name in its options.

    Used for ``account``/``category`` fields whose default ``__str__``
    includes the owner's e-mail (useful in the admin), which is redundant
    here since the queryset is already restricted to the logged-in user.
    """

    def label_from_instance(self, obj):
        return obj.name


class TransactionForm(forms.ModelForm):
    """Form used by an authenticated user to create or edit their own transactions.

    Requires the logged-in ``user`` to be passed in on instantiation so that
    the ``account`` and ``category`` field choices are restricted to objects
    owned by that user.
    """

    account = OwnedModelChoiceField(
        queryset=Account.objects.none(),
        widget=forms.Select(attrs={'class': INPUT_CLASSES}),
        label='Conta',
    )
    category = OwnedModelChoiceField(
        queryset=Category.objects.none(),
        widget=forms.Select(attrs={'class': INPUT_CLASSES}),
        label='Categoria',
    )
    transaction_date = forms.DateField(
        input_formats=['%Y-%m-%d'],
        widget=forms.DateInput(
            attrs={'class': INPUT_CLASSES, 'type': 'date'},
            format='%Y-%m-%d',
        ),
        label='Data',
    )

    class Meta:
        model = Transaction
        fields = (
            'description',
            'amount',
            'transaction_type',
            'account',
            'category',
            'transaction_date',
        )
        widgets = {
            'description': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'amount': forms.NumberInput(attrs={'class': INPUT_CLASSES, 'step': '0.01'}),
            'transaction_type': forms.Select(attrs={'class': INPUT_CLASSES}),
        }

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        if user is not None:
            self.fields['account'].queryset = Account.objects.filter(user=user)
            self.fields['category'].queryset = Category.objects.filter(user=user)
