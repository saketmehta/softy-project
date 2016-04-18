from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^profile/(?P<profile_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^profile/(?P<profile_id>[0-9]+)/messages/$', views.messages, name='messages'),
]