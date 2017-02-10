"""Quality App Views"""

from django.shortcuts import render

from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render 

### Quality Views
def index(request):
    """Quality Home Page"""

    return HttpResponse("Quality, baby!")

