from django.conf.urls import url
from ..views import NewsLinkCreate, NewsLinkUpdate

urlpatterns = [
    url(r'^create/$', NewsLinkCreate.as_view(), name='organizer_newslink_create'),
    url(r'^update/(?P<pk>\d+)/$', NewsLinkUpdate.as_view(), name='organizer_newslink_update'),
]
