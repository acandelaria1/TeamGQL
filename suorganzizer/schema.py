import graphene
from graphene import Schema, relay, resolve_only_args
from graphene_django import DjangoConnectionField, DjangoObjectType

from blog.models import Post as PostModel
from organizer.models import Tag as TagModel
from organizer.models import Startup as StartupModel
from organizer.models import NewsLink as NewsLinkModel

class Post(DjangoObjectType):
    
    class meta:
        model = PostModel

class Tag(DjangoObjectType):
    
    class meta:
        model = TagModel

class Startup(DjangoObjectType):
    
    class meta:
        model = StartupModel

class NewsLink(DjangoObjectType):
    
    class meta:
        model = NewsLinkModel
