"""Register and customize admin site"""

# Imports
from django.contrib import admin
from .models import RMA

# Register your models here.
admin.site.register(RMA)