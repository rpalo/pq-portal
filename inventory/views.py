from django.http import HttpResponse
from django.shortcuts import render
from .models import Plastic 
from .forms import PlasticForm


def index(request):
    plastics = Plastic.objects.all()
    context = {"plastics": plastics}
    return render(request, "inventory/index.html", context)

def add(request):

    if request.method == "POST":
        pass
    else:
        form = PlasticForm()
        return render(request, "inventory/form.html",
                        {"form": form})

def detail(request, id):
    return HttpResponse("It works!")

def delete(request, id):
    return HttpResponse("It works!")