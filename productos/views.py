from django.shortcuts import render
from .models import Productos

def lista_productos(request):
    """Muestra una lista de todos los productos."""
    # Obtiene todos los productos
    productos = Productos.objects.all().prefetch_related('embarques')
    
    context = {

        'productos': productos,
    }
    
    # Renderiza la plantilla
    return render(request, 'productos/lista.html', context)