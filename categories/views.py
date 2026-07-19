from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from categories.forms import CategoryForm
from categories.models import Category


class CategoryListView(LoginRequiredMixin, ListView):
    """List the categories belonging to the logged-in user."""

    model = Category
    template_name = 'categories/list.html'
    context_object_name = 'categories'

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)


class CategoryCreateView(LoginRequiredMixin, CreateView):
    """Create a new category for the logged-in user."""

    form_class = CategoryForm
    template_name = 'categories/form.html'
    success_url = reverse_lazy('categories:list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        response = super().form_valid(form)
        messages.success(self.request, 'Categoria criada com sucesso!')
        return response


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    """Update an existing category owned by the logged-in user."""

    form_class = CategoryForm
    template_name = 'categories/form.html'
    success_url = reverse_lazy('categories:list')

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Categoria atualizada com sucesso!')
        return response


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    """Delete a category owned by the logged-in user."""

    model = Category
    template_name = 'categories/confirm_delete.html'
    success_url = reverse_lazy('categories:list')

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Categoria excluída com sucesso!')
        return response
