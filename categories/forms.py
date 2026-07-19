from django import forms

from categories.models import Category


class CategoryForm(forms.ModelForm):
    """Form used by an authenticated user to create or edit their own categories."""

    class Meta:
        model = Category
        fields = ('name', 'category_type', 'color')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': (
                    'w-full rounded-lg border border-slate-300 px-3 py-2 text-sm text-slate-800 '
                    'focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent'
                ),
            }),
            'category_type': forms.Select(attrs={
                'class': (
                    'w-full rounded-lg border border-slate-300 px-3 py-2 text-sm text-slate-800 '
                    'focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent'
                ),
            }),
            'color': forms.TextInput(attrs={
                'type': 'color',
                'class': (
                    'h-10 w-16 rounded-lg border border-slate-300 p-1 '
                    'focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent'
                ),
            }),
        }
