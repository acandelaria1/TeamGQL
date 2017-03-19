from django.conf.urls import url
from organizer.urls import newslink as newslink_urls, startup as startup_urls, tag as tag_urls

urlpatterns = [
    url(r'^newslink/', include(newslink_urls)),
    url(r'^startup/', include(startup_urls)),
    url(r'^tag/', include(tag_urls)),
]

    '''url(r'^tag/$', tag_list, name='organizer_tag_list'),
    url(r'^tag/create/$', TagCreate.as_view(), name='organizer_tag_create'),
    url(r'^tag/(?P<slug>[\w\-]+)/update/$',TagUpdate.as_view(), name='organizer_tag_update'),
    url(r'^tag/(?P<slug>[\w\-]+)/delete/$', TagDelete.as_view(), name='organizer_tag_delete'),
    url(r'^tag/(?P<slug>[\w\-]+)/$', tag_detail, name='organizer_tag_detail'),
    url(r'^startup/$',startup_list, name='organizer_startup_list'),
    url(r'^startup/create/$', StartupCreate.as_view(), name='organizer_startup_create'),
    url(r'^startup/(?P<slug>[\w\-]+)/update/$', StartupUpdate.as_view(), name='organizer_startup_update'),
    url(r'^startup/(?P<slug>[\w\-]+)/delete/$', StartupDelete.as_view(), name='organizer_startup_delete'),
    url(r'^startup/(?P<slug>[\w\-]+)/$', startup_detail, name='organizer_startup_detail'),
    url(r'^newslink/create/$', NewsLinkCreate.as_view(), name='organizer_newslink_create'),
    url(r'^newslink/update/(?P<pk>\d+)/$', NewsLinkUpdate.as_view(), name='organizer_newslink_update'),
    '''
