import graphene
import books.query


class HelloQuery(graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")


class Query(
    books.query.Query,
    graphene.ObjectType
):
    pass


schema = graphene.Schema(query=Query)
