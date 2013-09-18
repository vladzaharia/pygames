from django.conf.urls import patterns, url

from gamesapp import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^details/(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^filter/type/(?P<game_type>.+)/$', views.TypeFilterView.as_view(), name='filter_type'),
    url(r'^filter/platform/(?P<platform>.+)/$', views.PlatformFilterView.as_view(), name='filter_platform'),
)