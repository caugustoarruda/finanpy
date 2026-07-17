from django.contrib import messages
from django.contrib.auth.views import LoginView as BaseLoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import LoginForm, SignUpForm
from users.models import User


class SignUpView(CreateView):
    """Public view that lets a visitor create a new account."""

    model = User
    form_class = SignUpForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(
            self.request, 'Cadastro realizado com sucesso! Faça login para continuar.'
        )
        return response


class LoginView(BaseLoginView):
    """Public view that authenticates a user via email and password."""

    form_class = LoginForm
    template_name = 'users/login.html'
    redirect_authenticated_user = True
