from django.conf.urls import url
from .views import PostUpdate, PostCreate, PostList, post_detail, PostDelete

urlpatterns = [
    url(r'^$',
        PostList.as_view(template_name='blog/post_list.html'),
        name='blog_post_list'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<slug>[\w\-]+)/update/$', PostUpdate.as_view(), name='blog_post_update'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<slug>[\w\-]+)/delete/$', PostDelete.as_view(), name='blog_post_delete'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<slug>[\w\-]+)/$', post_detail, {'parent_template':'base.html'}, name='blog_post_detail'),
    url(r'^create/$', PostCreate.as_view(), name='blog_post_create'),
]
