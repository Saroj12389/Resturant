from django.shortcuts import render
from django.views.generic import ListView,DetailView, CreateView, UpdateView, DeleteView
from.models import Items
from django.urls import reverse_lazy

# Create your views here.


# creating Home View 



class HomeView(ListView):
    template_name = 'home.html'
    model = Items
    context_object_name = 'items'




class ItemsDetailView(DetailView):
    model = Items
    template_name = 'items_detail.html'
    context_object_name = 'item'

    

