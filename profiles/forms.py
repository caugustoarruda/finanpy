from datetime import date

from django import forms

from profiles.models import Profile


class ISODateField(forms.DateField):
    """DateField that always displays its value in ISO 8601 (yyyy-mm-dd).

    The profile template renders `{{ field.value }}` directly (instead of
    `{{ field }}`), which skips the widget's `format_value()` and instead
    goes through Django's template auto-localization. With `pt-br` active,
    that turns a plain `date` object into "20 de Maio de 1990", which an
    HTML5 `<input type="date">` cannot parse, making the field look empty.
    Returning an ISO string from `prepare_value()` sidesteps that, since
    strings are never auto-localized by the template engine.
    """

    def prepare_value(self, value):
        if isinstance(value, date):
            return value.isoformat()
        return value


class ProfileForm(forms.ModelForm):
    """Form used by an authenticated user to edit their own profile."""

    birth_date = ISODateField(
        label='Data de nascimento',
        required=False,
        widget=forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
    )

    class Meta:
        model = Profile
        fields = ('phone', 'birth_date', 'avatar')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phone'].label = 'Telefone'
        self.fields['avatar'].label = 'Avatar (URL)'
