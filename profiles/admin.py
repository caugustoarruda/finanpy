from django.contrib import admin

from profiles.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Admin configuration for the Profile model."""

    list_display = ('user', 'phone', 'birth_date')
    search_fields = ('user__email', 'phone')
    readonly_fields = ('created_at', 'updated_at')
