import graphene
from graphene_django.types import DjangoObjectType

from organizer.models import Tag as TagModel
from organizer.models import Startup as StartupModel
from organizer.models import NewsLink as NewsLinkModel

class Tag(DjangoObjectType):
    class meta:
        model = TagModel

class Startup(DjangoObjectType):
    class meta:
        model = StartupModel

class NewsLink(DjangoObjectType):
    class meta:
        model = NewsLinkModel

