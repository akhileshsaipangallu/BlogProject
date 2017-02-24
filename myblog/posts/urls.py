from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.post_home, name='post_home'),
    url(r'^(?P<id>\d+)/$', views.post_details, name='post_details'),
    url(r'^create/$', views.post_form, name='post_form'),
    url(r'^(?P<id>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^(?P<id>\d+)/delete/$', views.post_delete, name='post_delete'),
]
