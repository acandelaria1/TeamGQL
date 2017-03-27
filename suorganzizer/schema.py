import graphene
from graphene import Schema, relay, resolve_only_args
from graphene_django import DjangoConnectionField, DjangoObjectType

from blog.models import Post as PostModel

class Post(DjangoObjectType):
    
    class meta:
        model = PostModel

