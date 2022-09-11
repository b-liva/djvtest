from django.urls import path

from theme.views import theme

urlpatterns = [
    path('theme', theme, name='theme')
]
