import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from books.models import Book, Author


class AuthorNode(DjangoObjectType):
    class Meta:
        model = Author
        filter_fields = {
            'first_name': ['exact', 'icontains', 'istartswith'],
            'last_name': ['exact', 'icontains'],
            'age': ['exact'],
        }
        interfaces = (graphene.relay.Node,)

    full_name = graphene.String()

    def resolve_full_name(self, info):
        return "%s by %s" % (self.first_name, self.last_name,)


class BookNode(DjangoObjectType):
    class Meta:
        model = Book
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'author__first_name': ['exact', 'icontains', 'istartswith'],
            'page': ['exact'],
            'exist': ['exact'],
        }
        interfaces = (graphene.relay.Node,)

    full_name = graphene.String()

    def resolve_full_name(self, info):
        return "%s by %s" % (self.name, self.author,)


class Query(graphene.ObjectType):
    all_authors = DjangoFilterConnectionField(AuthorNode)
    author = graphene.relay.Node.Field(AuthorNode)
    all_books = DjangoFilterConnectionField(BookNode)
    book = graphene.relay.Node.Field(BookNode)
