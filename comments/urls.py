from django.conf.urls import patterns, url
from comments import views

urlpatterns = patterns('',
  url(r'^$', views.home, name='home'),
  #url(r'^sentiment/$', views.sentiment, name='sentiment'),
)