from django.conf.urls import url
from . import views, apps
# app_name = 'music'


urlpatterns = [
	
	# /music/
    url(r'^$', views.IndexView.as_view(), name = "index"),
    url(r'^register/$', views.UserFormView.as_view(), name = "register"),



    # /music/<album_id>/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name = "detail"),

    #views.DetailView  is not a function.
    # to make it use as a function, we use .as_view()

    # /music/album/add
    url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),

    # /music/song/add
    url(r'song/add/$', views.SongCreate.as_view(), name='song-add'),
    url(r'song/$', views.SongIndexView.as_view(), name='song-index'),
    # url(r'song/(?P<pk>[0-9]+)/$', views.SongUpdate.as_view(), name='song-update'),
    # # /music/album_id/favourite/
    # url(r'^(?P<album_id>[0-9]+)/favourite/$', views.favourite, name = "favourite"),

    #/music/albujm/2/
    url(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-update'),
 	#/music/album/2/delete/
    url(r'album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),
   
]	