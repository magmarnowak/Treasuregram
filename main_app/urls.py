from django.conf.urls import url
# import the views module from the current app (main_app):
from . import views

urlpatterns = [
    url(r'^$', views.index),
]
