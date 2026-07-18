from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from profiles.forms import ProfileForm
from profiles.models import Profile


class ProfileDetailView(LoginRequiredMixin, UpdateView):
    """View that lets the logged-in user view and edit their own profile."""

    model = Profile
    form_class = ProfileForm
    template_name = 'profiles/detail.html'
    success_url = reverse_lazy('profiles:detail')

    def get_object(self, queryset=None):
        profile, _ = Profile.objects.get_or_create(user=self.request.user)
        return profile

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Perfil atualizado com sucesso!')
        return response
