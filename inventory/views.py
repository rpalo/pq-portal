"""View controller for the inventory application"""

# Imports
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .models import Batch, Log, Plastic, Part
from .forms import BatchForm, LogForm, PlasticForm, PartForm
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
                modLog = Log(plastic=plastic, change=qty, notes="Modified manually")
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
        messages.error(request, 'Cannot delete this plastic.  A part or batch exists that references this plastic.')
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
            if newLog.change > 0:
                newLog.change *= -1
            newLog.plastic.quantity += newLog.change
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

### Batch Views

# Show a list of all batches
def batchIndex(request):

    # Allow to filter by batch
    if request.GET.get('plastic'):
        plastic = Plastic.objects.get(pk=request.GET.get('plastic'))
        batches = Batch.objects.filter(plastic=plastic)
    else:
        batches = Batch.objects.all()
    return render(request, "inventory/batch-home.html",
                            {"batches": batches})

# Delete a specific batch
def deleteBatch(request, id):
    batch = get_object_or_404(Batch, pk=id)
    try:
        batch.delete()
    except ProtectedError:
        messages.error("Could not delete this batch.  There may be logs for this batch.  Delete those first.")
    return HttpResponseRedirect('/inventory/batches/')

# Add a new batch
def addBatch(request):

    # If the form was submitted
    if request.method == "POST":
        # Check if it is valid.  If so
        form = BatchForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the new batch
            newBatch = form.save()
            return HttpResponseRedirect('/inventory/batches/')
        else:
            return render(request, "inventory/batch-form.html",
                                    {"form": form})
    else:
    # Otherwise, show a blank form for a new batch
        form = BatchForm()
        return render(request, "inventory/batch-form.html",
                        {"form": form})

# Form to inspect/modify a batch
def batchDetail(request, id):
    batch = get_object_or_404(Batch, pk=id)

    # If the form has been submitted
    if request.method == "POST":
        # Make sure the form is valid
        form = BatchForm(request.POST, instance=batch)
        if form.is_valid():
            # save changes
            form.save()
            return HttpResponseRedirect('/inventory/batches/')
        else:
            raise Http404("Batch couldn't be modified.")
    else:
    # Otherwise, show form filled in with current batch data
        form = BatchForm(instance=batch)
        return render(request, 'inventory/batch-form.html',
                                {"form": form,
                                "batch": batch})

### Part Views

# List all parts
def partIndex(request):
    parts = Part.objects.all()
    return render(request, "inventory/part-home.html",
                            {"parts": parts})

# Delete a part
def deletePart(request, id):
    part = get_object_or_404(Part, pk=id)
    try:
        part.delete()
    except ProtectedError:
        messages.error("Could not delete part.  There may be a log that depends on this.  Delete those logs first.")
    return HttpResponseRedirect('/inventory/parts')

# Add a new part
def addPart(request):

    # If form was submitted
    if request.method == "POST":
        # Check if form is valid.  If so, 
        form  = PartForm(request.POST)
        if form.is_valid():
            # Save new part
            form.save()
            return HttpResponseRedirect("/inventory/parts/")
        else:
            return render(request, "inventory/part-form.html",
                            {"form": form})
    else:
        # Show blank form
        form = PartForm()
        return render(request, "inventory/part-form.html",
                        {"form": form})

# Modify a part
def partDetail(request, id):
    part = get_object_or_404(Part, pk=id)

    # If the form has been submitted
    if request.method == "POST":
        # Make sure the form is valid
        form = PartForm(request.POST, instance=part)
        if form.is_valid():
            # save changes
            form.save()
            return HttpResponseRedirect('/inventory/parts/')
        else:
            raise Http404("Batch couldn't be modified.")
    else:
    # Otherwise, show form filled in with current batch data
        form = PartForm(instance=part)
        return render(request, 'inventory/part-form.html',
                                {"form": form,
                                "part": part})