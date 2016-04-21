from django.conf.urls import url, include
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^accounts/login',  login),
    url(r'^accounts/logout', logout),
    url(r'^accounts/dashboard', views.dashboard, name='dashboard'),
]