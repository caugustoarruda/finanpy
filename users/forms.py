from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from users.models import User


class SignUpForm(UserCreationForm):
    """Form used by unauthenticated visitors to create a new account."""

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email', 'first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].label = 'E-mail'
        self.fields['email'].help_text = None
        self.fields['first_name'].label = 'Nome'
        self.fields['first_name'].required = True
        self.fields['last_name'].label = 'Sobrenome'
        self.fields['last_name'].required = False
        self.fields['password1'].label = 'Senha'
        self.fields['password2'].label = 'Confirmação de senha'

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError('Já existe uma conta com este e-mail.')
        return email


class LoginForm(AuthenticationForm):
    """Login form that authenticates using the user's email address."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'E-mail'
        self.fields['username'].widget = forms.EmailInput(
            attrs={'autofocus': True, 'autocomplete': 'email'}
        )
