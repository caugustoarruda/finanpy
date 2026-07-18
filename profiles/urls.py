from django.urls import path

from profiles.views import ProfileDetailView

app_name = 'profiles'

urlpatterns = [
    path('profile/', ProfileDetailView.as_view(), name='detail'),
]
