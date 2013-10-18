from django.conf.urls import patterns, url
from api import views

urlpatterns = patterns('',
  url(r'^$', views.home, name='home'),
  url(r'^comments/$', views.comments, name='comments'),
)