from django.contrib import admin

from categories.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Admin configuration for the Category model."""

    list_display = ('name', 'category_type', 'color', 'user')
    list_filter = ('category_type', 'user')
    search_fields = ('name',)
    readonly_fields = ('created_at', 'updated_at')
