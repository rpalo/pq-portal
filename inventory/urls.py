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
]