import graphene
from graphene import Schema, relay, resolve_only_args
from graphene_django import DjangoConnectionField, DjangoObjectType

from blog.models import Post as PostModel

class Post(DjangoObjectType):
    
    class Meta:
        model = PostModel

class Query(graphene.AbstractType):
    all_posts = graphene.List(PostModel)
    
    def resolve_all_posts(self, args, context, info):
        return PostModel.objects.all()
