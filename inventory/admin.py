"""Register and customize the admin site here"""

# Imports
from django.contrib import admin
from .models import Batch, Log, Plastic


# Register Models
admin.site.register(Batch)
admin.site.register(Plastic)
admin.site.register(Log)
