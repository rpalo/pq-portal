"""Register and customize the admin site here"""

# Imports
from django.contrib import admin
from .models import Log, Plastic


# Register Models
admin.site.register(Plastic)
admin.site.register(Log)
