from django.conf.urls import patterns, url

from jsDashboard import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<dboard_id>\w+)/$', views.detail, name='detail'),
)
