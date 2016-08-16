from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .models import Log, Plastic
from .forms import LogForm, PlasticForm


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
        form = PlasticForm(instance=plastic)
        return render(request, "inventory/plastic-form.html",
                                    {"form": form,
                                    "plastic": plastic})

    return HttpResponse("It works!")

def delete(request, id):
    plastic = get_object_or_404(Plastic, pk=id)
    plastic.delete()
    return HttpResponseRedirect("/inventory/")

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
    log = get_object_or_404('Log', pk=id)
    log.delete()
    return HttpResponseRedirect('/inventory/logs')