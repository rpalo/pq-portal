from django.conf.urls import url 

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add/$', views.add, name='add'),
    url(r'^detail/(?P<id>[0-9]+)/$', views.detail),
    url(r'^delete/(?P<id>[0-9]+)/$', views.delete),
]