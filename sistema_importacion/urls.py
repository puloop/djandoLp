
from django.contrib import admin
from django.urls import path , include
from productos.views import PaginaPrincipal

urlpatterns = [
    path('', PaginaPrincipal.as_view(), name='home'),
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('productos/', include('productos.urls'))
]
