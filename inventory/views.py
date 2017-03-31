"""View controller for the inventory application"""

# Imports
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .models import Log, Plastic
from .forms import LogForm, PlasticForm
from django.db.models import ProtectedError
from django.contrib import messages

### Plastics Views

# Home Page
def index(request):
    plastics = Plastic.objects.all().order_by('quantity')
    context = {"plastics": plastics}
    return render(request, "inventory/index.html", context)

# Add new plastic
def add(request):
    # If user has submitted form
    if request.method == "POST":
        # Check it for validity.  If Valid
        form = PlasticForm(request.POST)
        if form.is_valid():
            # Create new plastic and log the creation
            newPlastic = form.save()
            firstLog = Log(change=newPlastic.quantity, notes="Added new plastic")
            firstLog.save()
            return HttpResponseRedirect('/inventory/')
        else:
            raise Http404("There was a problem adding the plastic.")
    else:
    # Otherwise, show the blank form
        form = PlasticForm()
        return render(request, "inventory/plastic-form.html",
                        {"form": form})

# View the details of plastics, and update if need be
def detail(request, id):
    plastic = get_object_or_404(Plastic, pk=id)
    # If user submitted form
    if request.method == "POST":
        form = PlasticForm(request.POST, instance=plastic)
        # Check it for validity
        if form.is_valid():
            # If user changed the qty
            qty = form.cleaned_data['quantity']
            if qty != plastic.quantity:
                modLog = Log(plastic=plastic, new_value=qty)
                modLog.save()
            # log the change, then save
            form.save()
            return HttpResponseRedirect('/inventory/')
        else:
            raise Http404("Plastic couldn't be updated.")
    else:
    # Otherwise show the form with the current record
        form = PlasticForm(instance=plastic)
        return render(request, "inventory/plastic-form.html",
                                    {"form": form,
                                    "plastic": plastic})

# Delete a plastic
def delete(request, id):
    plastic = get_object_or_404(Plastic, pk=id)
    try:
        plastic.delete()
    except ProtectedError:
        messages.error(request, 'Cannot delete this plastic.  A log exists that references this plastic.')
    return HttpResponseRedirect("/inventory/")

### Log Views

# Add new log 
def addLog(request):
    # If form has been submitted
    if request.method == "POST":
        # Make sure it is valid.  if so
        form = LogForm(request.POST)
        if form.is_valid():
            # Make the new log, but, assuming most logs will be plastic use,
            # ensure logs can only subtract plastic
            newLog = form.save(commit=False)
            newLog.plastic.quantity = newLog.new_value
            newLog.plastic.save()
            newLog.save()
            return HttpResponseRedirect(newLog.plastic.get_absolute_url())
        else:
            return render(request, "inventory/log-form.html",
                        {"form": form})
    else:

    # Otherwise, show the blank log form
        form = LogForm()
        return render(request, "inventory/log-form.html",
                                {"form": form})

# Log home page, shows all logs
def logIndex(request, plastic=None):
    # Allow for filter by plastic
    if plastic:
        logs = Log.objects.filter(plastic=plastic).order_by('-timestamp')
    else:
        logs = Log.objects.all().order_by('-timestamp')
    return render(request, "inventory/log-home.html",
                                {"logs": logs,
                                "plastic": plastic})

# Delete a specific log
def deleteLog(request, id):
    log = get_object_or_404(Log, pk=id)
    try:
        log.delete()
    except ProtectedError:
        messages.error("Could not delete this log.  It may have children that depend on it.")
    return HttpResponseRedirect('/inventory/logs')

