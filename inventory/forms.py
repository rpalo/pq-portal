from django.forms import ModelForm
from .models import Plastic, Log

class PlasticForm(ModelForm):

    class Meta:
        model = Plastic
        exclude = []

class LogForm(ModelForm):

	class Meta:
		model = Log
		exclude = ['timestamp']