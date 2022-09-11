"""gqltest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt

from books.views import PrivateGraphQLView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('books.urls')),
    path('themes/', include('theme.urls')),
    path("graphql", csrf_exempt(PrivateGraphQLView.as_view(graphiql=True))),
    path("__reload__/", include("django_browser_reload.urls")),
]
