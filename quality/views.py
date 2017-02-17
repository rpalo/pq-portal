"""Quality App Views"""

from .models import RMA
from django.contrib import messages
from django.db.models import ProtectedError
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render 

### Quality Views
def index(request):
    """Quality Home Page"""

    return HttpResponse("Quality, baby!")

def rma_index(request):
    """Main List of RMA's"""
    rmas = RMA.objects.all().order_by('-open')
    context = {"rmas": rmas}
    return render(request, "quality/rma/index.html", context)

def rma_delete(request, pk):
    """Delete a specific rma"""

    rma = get_object_or_404(RMA, pk=id)
    try:
        rma.delete()
    except ProtectedError:
        messages.error(request, 'Cannot delete this RMA.  There is something that references it.')
    return HttpResponseRedirect("/quality/rma/")

