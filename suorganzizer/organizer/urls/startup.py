from django.conf.urls import url
from ..views import StartupList, StartupCreate, StartupUpdate, StartupDelete, startup_detail

urlpatterns = [
    url(r'^$', StartupList.as_view(), name='organizer_startup_list'),
    url(r'^create/$', StartupCreate.as_view(), name='organizer_startup_create'),
    url(r'^(?P<slug>[\w\-]+)/update/$', StartupUpdate.as_view(), name='organizer_startup_update'),
    url(r'^(?P<slug>[\w\-]+)/delete/$', StartupDelete.as_view(), name='organizer_startup_delete'),
    url(r'^(?P<slug>[\w\-]+)/$', startup_detail, name='organizer_startup_detail'),

]







