from django.urls import path
from . import views # Importa las vistas de tu app productos
from productos.views import PaginaPrincipal

app_name = 'productos' # Define el espacio de nombres [cite: 204]

urlpatterns = [
    # Ruta inicial para el listado de productos [cite: 207]
    path('', views.ListaProducto.as_view(), name='lista_productos'),
    path('', PaginaPrincipal.as_view(), name='home'),
]