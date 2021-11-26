from django.conf.urls import url

from . import views


urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^players/$', views.PlayerListView.as_view(), name='players'),
        url(r'^player/(?P<pk>[0-9A-Za-z-]+)/$', views.PlayerDetailView.as_view(), name='player-detail'),
        ]

