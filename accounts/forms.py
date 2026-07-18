from django import forms

from accounts.models import Account


class AccountForm(forms.ModelForm):
    """Form used by an authenticated user to create or edit their own accounts."""

    class Meta:
        model = Account
        fields = ('name', 'account_type', 'initial_balance')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': (
                    'w-full rounded-lg border border-slate-300 px-3 py-2 text-sm text-slate-800 '
                    'focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent'
                ),
            }),
            'account_type': forms.Select(attrs={
                'class': (
                    'w-full rounded-lg border border-slate-300 px-3 py-2 text-sm text-slate-800 '
                    'focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent'
                ),
            }),
            'initial_balance': forms.NumberInput(attrs={
                'class': (
                    'w-full rounded-lg border border-slate-300 px-3 py-2 text-sm text-slate-800 '
                    'focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent'
                ),
                'step': '0.01',
            }),
        }
