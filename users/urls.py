from django.conf.urls import url, include
from . import views
from django.contrib.auth.views import login, logout, password_change, password_change_done

urlpatterns = [
    url(r'^accounts/login/$',  login, name='login'),
    url(r'^accounts/logout/$', views.logout_view, name='logout'),
    url(r'^accounts/password_change/done/$', password_change_done, name='password_change_done'),
    url(r'^accounts/password_change/$', password_change, {'post_change_redirect': 'done/'}, name='password_change'),
    url(r'^accounts/register/$', views.register, name='register'),
    url(r'^accounts/dashboard/$', views.dashboard, name='dashboard'),
]