"""Basic url routing for the entire portal"""

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html')),   # Main portal page
    url(r'^admin/', admin.site.urls),                               # Admin site
    url(r'^inventory/', include('inventory.urls')),                  # Inventory App
    url(r'^quality/', include('quality.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)   # Include uploaded media files
