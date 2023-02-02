from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('settings', views.settings, name='settings'),
    path('upload', views.upload, name='upload'),
    re_path(r'^client/(?P<id_user>[0-9]+)$', views.client, name= 'client'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('logout', views.logout, name='logout'),
    re_path(r'^preedit/(?P<pk>[0-9]+)$', views.preedit, name='preedit'),
    re_path(r'^edit/(?P<pk>[0-9]+)$', views.edit, name='edit'),
    re_path(r'^delete/(?P<pk>[0-9]+)$', views.delete, name='delete'),
    path('search', views.search, name='search'),
]
