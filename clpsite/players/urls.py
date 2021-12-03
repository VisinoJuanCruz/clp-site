from django.conf.urls import url

from . import views


urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^players/$', views.PlayerListView.as_view(), name='players'),
        url(r'^player/(?P<pk>[0-9A-Za-z-]+)/$', views.PlayerDetailView.as_view(), name='player-detail'),
        ]
urlpatterns += [
        url(r'^agents/$', views.AgentListView.as_view(), name='agents'),
        url(r'^agent/(?P<pk>[0-9A-Za-z-]+)/$', views.AgentDetailView.as_view(), name='agent-detail'),
        url(r'^maps/$', views.MapListView.as_view(), name='maps'),
        url(r'^map/(?P<pk>[0-9A-Za-z-]+)/$', views.MapDetailView.as_view(), name='map-detail'),
        ]
urlpatterns +=[
        url('upload_image/',views.upload_image, name='upload_image'),
        ]
