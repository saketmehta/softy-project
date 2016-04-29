from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^account/dashboard/$', views.dashboard, name='dashboard'),
    url(r'^account/history/$', views.history, name='history'),
    url(r'^account/ask/$', views.ask, name='ask'),
    url(r'^account/question/(?P<question_id>[0-9]+)/$', views.question_details, name='question-details'),
    url(r'^account/answer/$', views.answer, name='answer'),
]