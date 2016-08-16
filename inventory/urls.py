from django.conf.urls import url 

from . import views

urlpatterns = [
    url(r'^$', views.index, name='plastic-home'),
    url(r'^add/$', views.add, name='add'),
    url(r'^detail/(?P<id>[0-9]+)/$', views.detail),
    url(r'^delete/(?P<id>[0-9]+)/$', views.delete, name='delete'),
    url(r'^logs/$', views.logIndex, name='log-home'),
    url(r'^logs/add/$', views.addLog, name='add-log'),
    url(r'^logs/delete/(?P<id>[0-9]+)/$', views.deleteLog, name='delete-log'),
    url(r'^batches/$', views.batchIndex, name='batch-home'),
    url(r'^batches/delete/(?P<id>[0-9]+)/$', views.deleteBatch, name='delete-batch'),
    url(r'^batches/add/$', views.addBatch, name='add-batch'),
    url(r'^batches/(?P<id>[0-9]+)/$', views.batchDetail, name='batch-detail'),
]