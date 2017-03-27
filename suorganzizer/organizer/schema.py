import graphene
from graphene_django.types import DjangoObjectType

from organizer.models import Tag as TagModel
from organizer.models import Startup as StartupModel
from organizer.models import NewsLink as NewsLinkModel

class Tag(DjangoObjectType):
    class Meta:
        model = TagModel

class Startup(DjangoObjectType):
    class Meta:
        model = StartupModel

class NewsLink(DjangoObjectType):
    class Meta:
        model = NewsLinkModel

class Query(graphene.AbstractType):
    
    all_tags = graphene.List(Tag)
    all_startups = graphene.List(Startup)
    all_newslinks = graphene.List(NewsLink)

    def resolve_all_tags(self, args, context, info):
        return TagModel.objects.all()

    def resolve_all_startups(self, args, context, info):
        return StartupModel.objects.all()

    def resolve_all_newslinks(self, args, context, info):
        return NewsLinkModel.objects.all()
