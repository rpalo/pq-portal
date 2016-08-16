from django.contrib import admin
from .models import Batch, Log, Plastic

admin.site.register(Batch)
admin.site.register(Plastic)
admin.site.register(Log)
