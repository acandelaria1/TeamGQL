import graphene
import suorganizer.blog.schema
import suorganizer.organizer.schema


class Query(suroganizer.blog.schema, suorganizer.organizer.schema, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)

