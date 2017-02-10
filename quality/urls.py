"""URL Routing for Quality App"""

from django.conf.urls import url

from . import views

urlpatterns = [
    # Quality home page
    url(r'^$', views.index, name='quality-home'),
]