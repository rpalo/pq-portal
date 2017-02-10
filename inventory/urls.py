"""URL Routing for Plastic Inventory"""

from django.conf.urls import url

from . import views

urlpatterns = [
    # Plastic Home Page/Main App Home Page
    url(r'^$', views.index, name='plastic-home'),
    # Add a new plastic
    url(r'^add/$', views.add, name='add'),
    # View/modify specific plastic
    url(r'^detail/(?P<id>[0-9]+)/$', views.detail),
    # Delete specific plastic
    url(r'^delete/(?P<id>[0-9]+)/$', views.delete, name='delete'),
    # Logs Home/List all Logs
    url(r'^logs/$', views.logIndex, name='log-home'),
    # Add new log
    url(r'^logs/add/$', views.addLog, name='add-log'),
    # Delete specific log
    url(r'^logs/delete/(?P<id>[0-9]+)/$', views.deleteLog, name='delete-log'),
    # Batches Home/List all batches (or filtered batches)
    url(r'^batches/$', views.batchIndex, name='batch-home'),
    # Delete a specific batch
    url(r'^batches/delete/(?P<id>[0-9]+)/$', views.deleteBatch, name='delete-batch'),
    # Add a new batch
    url(r'^batches/add/$', views.addBatch, name='add-batch'),
    # View details/modify specific batch
    url(r'^batches/(?P<id>[0-9]+)/$', views.batchDetail, name='batch-detail'),
    # Parts Home/List all parts
    url(r'^parts/$', views.partIndex, name="part-home"),
    # Add new part
    url(r'^parts/add/$', views.addPart, name="add-part"),
    # Modify Part
    url(r'^parts/(?P<id>[0-9]+)/$', views.partDetail, name="part-detail"),
    # Delete part
    url(r'^parts/delete/(?P<id>[0-9]+)/$', views.deletePart, name="delete-part"),
]