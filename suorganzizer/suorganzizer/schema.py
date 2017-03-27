import graphene
from blog import schema as blog_schema
from organizer import schema as organizer_schema

class Query(organizer_schema.Query, blog_schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)

