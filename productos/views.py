from django.shortcuts import render
from .models import Productos , Embarque ,Categoria
from django.views.generic import TemplateView, ListView


class PaginaPrincipal(TemplateView):
    template_name = 'Principal.html'

    
class ListaProducto(ListView):
    queryset = Categoria.objects.get(id = 1)
    model = Categoria
    template_name = 'productos/lista.html'
    context_object_name = 'categoria'
