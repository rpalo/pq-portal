"""Model-based forms and their customization"""

from django.forms import ModelForm
from .models import Batch, Plastic, Log, Part

class PlasticForm(ModelForm):

    class Meta:
        model = Plastic
        exclude = []

class LogForm(ModelForm):

	class Meta:
		model = Log
		exclude = ['timestamp']

class BatchForm(ModelForm):

	class Meta:
		model = Batch
		exclude = ['date_added']

class PartForm(ModelForm):

	class Meta:
		model = Part
		exclude = []