from django.shortcuts import render
from .models import Productos , Embarque
from django.views.generic import TemplateView, ListView

class ListaProducto(ListView):
    model = Productos
    template_name = 'producto'
        