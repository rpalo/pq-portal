"""URL Routing for Quality App"""

from django.conf.urls import url

from . import views

urlpatterns = [
    # Quality home page
    url(r'^$', views.index, name='quality-home'),
    url(r'^rma/$', views.rma_index, name='rma-home'),
    url(r'^rma/delete/(?P<pk>[0-9]+)/$', views.rma_delete, name='rma-delete'),
]