from django.urls import path, include

from books.views import index

urlpatterns = [
    path('index', index, name='index')
]
