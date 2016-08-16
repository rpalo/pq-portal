from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .models import Plastic 
from .forms import PlasticForm


def index(request):
    plastics = Plastic.objects.all()
    context = {"plastics": plastics}
    return render(request, "inventory/index.html", context)

def add(request):

    if request.method == "POST":
        form = PlasticForm(request.POST)
        if form.is_valid():
            newPlastic = form.save()

            return HttpResponseRedirect('/inventory/')
    else:
        form = PlasticForm()
        return render(request, "inventory/form.html",
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
        return render(request, "inventory/form.html",
                                    {"form": form,
                                    "plastic": plastic})

    return HttpResponse("It works!")

def delete(request, id):
    plastic = get_object_or_404(Plastic, pk=id)
    plastic.delete()
    return HttpResponseRedirect("/inventory/")