from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .models import Batch, Log, Plastic
from .forms import BatchForm, LogForm, PlasticForm

### Plastics Views
def index(request):
    plastics = Plastic.objects.all().order_by('quantity')
    context = {"plastics": plastics}
    return render(request, "inventory/index.html", context)

def add(request):

    if request.method == "POST":
        form = PlasticForm(request.POST)
        if form.is_valid():
            newPlastic = form.save()
            firstLog = Log(plastic=newPlastic, change=newPlastic.quantity, notes="Added new plastic")
            firstLog.save()
            return HttpResponseRedirect('/inventory/')
        else:
            raise Http404("There was a problem adding the plastic.")
    else:
        form = PlasticForm()
        return render(request, "inventory/plastic-form.html",
                        {"form": form})

def detail(request, id):
    plastic = get_object_or_404(Plastic, pk=id)
    if request.method == "POST":
        form = PlasticForm(request.POST, instance=plastic)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/inventory/')
        else:
            raise Http404("Plastic couldn't be updated.")
    else:
        form = PlasticForm(instance=plastic)
        return render(request, "inventory/plastic-form.html",
                                    {"form": form,
                                    "plastic": plastic})

    return HttpResponse("It works!")

def delete(request, id):
    plastic = get_object_or_404(Plastic, pk=id)
    plastic.delete()
    return HttpResponseRedirect("/inventory/")

### Log Views
def addLog(request):
    if request.method == "POST":
        form = LogForm(request.POST)
        if form.is_valid():
            newLog = form.save(commit=False)
            if newLog.change > 0:
                newLog.change *= -1
            newLog.plastic.quantity += newLog.change
            newLog.plastic.save()
            newLog.save()
            return HttpResponseRedirect(newLog.plastic.get_absolute_url())
        else:
            raise Http404("Log couldn't be added")
    else:
        form = LogForm()
        return render(request, "inventory/log-form.html",
                                {"form": form})

def logIndex(request, plastic=None):
    if plastic:
        logs = Log.objects.filter(plastic=plastic).order_by('-timestamp')
    else:
        logs = Log.objects.all().order_by('-timestamp')
    return render(request, "inventory/log-home.html",
                                {"logs": logs,
                                "plastic": plastic})

def deleteLog(request, id):
    log = get_object_or_404(Log, pk=id)
    log.delete()
    return HttpResponseRedirect('/inventory/logs')

### Batch Views

def batchIndex(request):
    if request.GET.get('plastic'):
        plastic = Plastic.objects.get(pk=request.GET.get('plastic'))
        batches = Batch.objects.filter(plastic=plastic)
    else:
        batches = Batch.objects.all()
    return render(request, "inventory/batch-home.html",
                            {"batches": batches})

def deleteBatch(request, id):
    batch = get_object_or_404(Batch, pk=id)
    batch.delete()
    return HttpResponseRedirect('/inventory/batches/')

def addBatch(request):
    if request.method == "POST":
        form = BatchForm(request.POST, request.FILES)
        if form.is_valid():
            newBatch = form.save()
            return HttpResponseRedirect('/inventory/batches/')
        else:
            return render(request, "inventory/batch-form.html",
                                    {"form": form})
    else:
        form = BatchForm()
        return render(request, "inventory/batch-form.html",
                        {"form": form})

def batchDetail(request, id):
    batch = get_object_or_404(Batch, pk=id)
    if request.method == "POST":
        form = BatchForm(request.POST, instance=batch)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/inventory/batches/')
        else:
            raise Http404("Batch couldn't be modified.")
    else:
        form = BatchForm(instance=batch)
        return render(request, 'inventory/batch-form.html',
                                {"form": form,
                                "batch": batch})