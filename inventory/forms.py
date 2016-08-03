from django.forms import ModelForm
from .models import Plastic

class PlasticForm(ModelForm):

    class Meta:
        model = Plastic
        exclude = []