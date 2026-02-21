from django.urls import path
from . import views # Importa las vistas de tu app productos

app_name = 'productos' # Define el espacio de nombres [cite: 204]

urlpatterns = [
    # Ruta inicial para el listado de productos [cite: 207]
    path('', views.lista_productos, name='lista_productos'),
]