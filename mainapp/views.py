from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView
from .models import *
from django.urls import reverse_lazy,reverse
from .forms import NavigationForm

# Create your views here.

def home(request):
    return render(request,'index.html')


class ListVehicle(ListView):
    template_name = "listvehicle.html"
    model = Navigation
    context_object_name = 'vehicle'


class DetailVehicle(DetailView):
    template_name = "detailvehicle.html"
    model = Navigation
    context_object_name = "vehicle"

class CreateVehicle(CreateView):
    template_name = "addvehicle.html"
    form_class = NavigationForm
    success_url = reverse_lazy("navigation")

class UpdateVehicle(UpdateView):
    model = Navigation
    template_name = "updatevehicle.html"
    form_class = NavigationForm
    success_url = reverse_lazy("navigation")