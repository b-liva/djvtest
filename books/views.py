from django.contrib.auth.mixins import LoginRequiredMixin
from graphene_django.views import GraphQLView
from django.shortcuts import render

# Create your views here.
from books.models import Book


class PrivateGraphQLView(LoginRequiredMixin, GraphQLView):
    pass


def index(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, 'books/index.html', context)
