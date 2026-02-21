from django.contrib import admin
from .models import Productos, Categoria, Embarque


class EmbarqueAdmin(admin.ModelAdmin):
    filter_horizontal = ('productos',)

admin.site.register(Categoria)
admin.site.register(Productos)
admin.site.register(Embarque, EmbarqueAdmin)
