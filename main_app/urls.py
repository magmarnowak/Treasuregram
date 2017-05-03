from django.conf.urls import url
# import the views module from the current app (main_app):
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^([0-9]+)/$', views.detail, name = 'detail'),
    url(r'^post_url/$', views.post_treasure, name='post_treasure'),
]
